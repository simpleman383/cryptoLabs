from Crypto.Cipher import AES
from Crypto import Random
from task1 import pkcs7
import base64
import random
from math import gcd


def getInputString(my_string):
    prefix = b""
    for i in range(random.randint(1,1000)):
        prefix += bytes.fromhex(hex(random.randint(30,100))[2:].zfill(2))
    res = prefix + str(my_string).encode() + base64.b64decode(unknownBase64String)
    return pkcs7(res.decode(), AES.block_size)

def encryptECB(input_string, key):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(input_string)
    return result

def findUnknownBytes(blockSize):
    while True:
        attack = getInputString(2 * AES.block_size * 'X')
        enc = encryptECB(attack, key)
        for flt in range(1,10):
            if enc[flt*blockSize:(flt+1)*blockSize] == enc[(flt+1)*blockSize:(flt+2)*blockSize]:
                return attack[(flt+2)*blockSize:]

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

def get_block_size():
    length = 0
    for i in range(1000):
        attack_cipher_text = encryptECB(getInputString("X" * random.randint(0, i)), key)
        length = gcd(len(attack_cipher_text), length)
    return length

unknownBase64String = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
key = Random.new().read(AES.block_size)
blockSize = AES.block_size

unknownStringBytes = findUnknownBytes(AES.block_size)

result = b""
for i in range(len(unknownStringBytes) // blockSize):
    result += bruteForceBlock(unknownStringBytes[i*blockSize:(i+1)*blockSize], blockSize)

print("RESULT ",  result)
