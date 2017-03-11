import re
import random
from task1 import pkcs7
from task1 import pkcs7_check
from Crypto.Cipher import AES
from Crypto import Random

def ParseStringToObject(string):
    splitted = str(string).split('&')
    template = re.compile("(\w+=\w+){1}")
    obj = {}
    for item in splitted:
        success = template.match(item)
        if not success:
            print('format error')
            return None
        key_value = item.split('=')
        obj[key_value[0]] = key_value[1]
    return obj

def profileFor(email):
    if str(email).count('&') != 0 or str(email).count('=') != 0:    #хорошо бы написать нормальный обработчик, но похуй
        print('format error')
        return None
    obj = {}
    obj['email'] = email
    obj['uid'] = random.randint(0,100)
    obj['role'] = 'user'

    return 'email=' + obj['email'] + '&' + 'uid=' + str(obj['uid']) + '&' + 'role=' + obj['role']

def encryptECB(input_string, key):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(input_string)
    return result

def decryptECB(input_string, key):
    if (len(key) != 16) or len(input_string) % 16 != 0:
        print("ERROR: encryptECB")
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.decrypt(input_string)
    return result

key = Random.new().read(AES.block_size)
imitation = b""
plain_text = profileFor('akurnev@ya.ru')
encrypted_text = encryptECB(pkcs7(plain_text, AES.block_size), key)

print(ParseStringToObject(pkcs7_check(decryptECB(encrypted_text, key)).decode()))

imitation+=encrypted_text[:32]

plain_text = profileFor('akurnev@yaadmin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b')

encrypted_text = encryptECB(pkcs7(plain_text, AES.block_size), key)
imitation+=encrypted_text[16:32]

result = decryptECB(imitation, key)
print(ParseStringToObject(pkcs7_check(result).decode()))

