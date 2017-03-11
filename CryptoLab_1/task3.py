from Crypto.Cipher import AES
from Crypto import Random
from task1 import pkcs7
from task1 import toHex

def getInputString(input_string):
    #input_string = str(input_string).replace('=','').replace(';','')
    input_string = "comment1=cooking%20MCs;userdata=" + input_string + ";comment2=%20like%20a%20pound%20of%20bacon"
    return pkcs7(input_string ,AES.block_size)

def encryptCBC(input_string, key, iv):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.encrypt(input_string)
    return result

def decryptCBC(input_string, key, iv):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.decrypt(input_string)


    return result

def searchTemplate(decrypted_text, template):
    if decrypted_text.count(template) != 0:
        print("SUCCESS: ", decrypted_text)
        return True
    return False

def decryptECB(input_string, key):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.decrypt(input_string)
    return result



def xor_blocks(block1, block2):
    if len(block1) != len(block2):
        print("XOR ERROR")
        return None
    res = ""
    for b1, b2 in zip(block1,block2):
        res += chr( b1 ^ b2 )
    return bytes.fromhex(toHex(res))



key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)
data = "admin=false"
template = b"admin=true;comme"

data = getInputString(data)
print("PLAIN_TEXT: ",data)

encrypted_text = encryptCBC(data, key, iv)
print("ENCRYPTED_TEXT: ",encrypted_text)

custom_block = encrypted_text[32:48]
decrypted_c_block = decryptECB(custom_block,key)

prev_encr_block = encrypted_text[16:32]

imitation = xor_blocks(decrypted_c_block, template)

encrypted_text = encrypted_text[:16] + imitation + encrypted_text[32:]
print("ATTACK RESULT:", decryptCBC(encrypted_text,key,iv))





