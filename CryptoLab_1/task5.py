from Crypto.Cipher import AES
from Crypto import Random
from task1 import pkcs7
import base64


def getInputString(my_string):
    res = str(my_string).encode() + base64.b64decode(unknownBase64String)
    return pkcs7(res.decode(), AES.block_size)

def encryptECB(input_string, key):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(input_string)
    return result

def detectBlockSize(key):
    k = 1
    while True:
        temp = 'A'*k
        encrypted_text = encryptECB(getInputString(temp), key)
        if encrypted_text[: k // 2] == encrypted_text[k // 2 : k]:
            return k // 2
        k+=1
    return -1

def bruteForceBlock(unknown_block, blockSize):
    plain_block = b""
    for length in range(1, blockSize + 1):
        example = ('X' * (blockSize - length)).encode() + unknown_block[:length]
        for byte in range(255):
            xxx = 'X' * (blockSize - len(plain_block) - 1)
            brute_string = xxx.encode() + plain_block + chr(byte).encode()
            if encryptECB(example, key) == encryptECB(brute_string, key):
                plain_block += chr(byte).encode()
                break;
    return plain_block


unknownBase64String = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
key = Random.new().read(AES.block_size)
blockSize = detectBlockSize(key)

unknownStringBytes = getInputString('')
result = b""

for i in range(len(unknownStringBytes) // blockSize):
    result += bruteForceBlock(unknownStringBytes[i*blockSize:(i+1)*blockSize], blockSize)

print("RESULT ",  result)


