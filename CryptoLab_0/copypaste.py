from Crypto.Cipher import AES
from hashlib import md5
import hex_base64_converter

def toASCII(buf):
    decrypted_text = ""
    splited_byte_blocks = []
    index = 0
    while index < len(buf):
        hex_block = buf[index: index + 2]
        splited_byte_blocks.append(hex_block)
        index = index + 2

    for byte in splited_byte_blocks:
        decrypted_text += chr(int(byte, 16))
    return  decrypted_text


def toHex(key):
    res = ""
    for i in key:
        if ord(i) < 16:
            ff = "0" + hex(ord(i))[2:]
        else:
            ff = hex(ord(i))[2:]
        res += str(ff)
    return res


def expand_key(key_string, salt, key_length):
    key_expanded = ""
    while len(key_expanded) < key_length + AES.block_size:
        key_expanded += str(md5(bytes.fromhex(toHex(key_expanded + key_string + salt))).hexdigest())
    return key_expanded[:key_length*2]


def task7_demo():
    with open("decryptAesEcb.txt", "r") as decrypt_aes_ecb:
        base64_strings = decrypt_aes_ecb.readlines()
    base64_strings = [x.strip() for x in base64_strings]

    cipher_text = "".join(base64_strings)
    cipher_text_hex = hex_base64_converter.toHex(cipher_text)
    cipher_text_ascii = toASCII(cipher_text_hex)

    #print("ASCII SOUCRE CIPHER TEXT:")
   #print(cipher_text_ascii)


    salt = cipher_text_ascii[:AES.block_size][len('Salted__'):]

    print("ASCII SALT:")
    print(toHex(salt))


    print("expanding key......")
    key = expand_key("YELLOW SUBMARINE", salt, 16)
    print("KEY: ", key)

    cipher = AES.new(bytes.fromhex(key),AES.MODE_ECB)
    print("DECRYPTED_TEXT:")
    print(cipher.decrypt(bytes.fromhex(cipher_text_hex)))


