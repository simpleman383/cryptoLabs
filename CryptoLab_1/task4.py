from Crypto.Cipher import AES
from Crypto import Random
from task1 import pkcs7
from task1 import toHex
import random

def getInputString(input_string):
    range_left = random.randint(5,10)
    range_right = random.randint(5,10)
    res = ""

    for i in range(range_left):
        res += chr(random.randint(0,1))

    res+=input_string

    for i in range(range_right):
        res+=chr(random.randint(0,1))
    return pkcs7(res, 16)


def encryptECB(input_string, key):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    key = key.encode()
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(input_string)
    return result


def encryptCBC(input_string, key):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    key = key.encode()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.encrypt(input_string)
    return result


def randomCipher(input_string, key):
    mode_index = random.randint(0,1)
    if mode_index == 1:
        result = encryptECB(input_string, key)
    else:
        result = encryptCBC(input_string, key)
    return result


def detectECB(item):
    item = toHex(str(item))

    splited_byte_blocks = []
    index = 0
    while index < len(item):
        block = item[index: index + 32]
        splited_byte_blocks.append(block)
        index = index + 32

    for block in splited_byte_blocks:
        n = item.count(block)
        if n > 1:
            print("SUCCESS: ECB MODE DETECTED!!! " , item)
            return True
    return False


key = "YELLOW SUBMARINE"
for it in range(100):
    input_string = "123456789YELLOW SUBMARINE12345678________YELLOW SUBMARINE"
    input_string = getInputString(input_string)
    #print(input_string)
    result = randomCipher(input_string,key)
    detectECB(result)