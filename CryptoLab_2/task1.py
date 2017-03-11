import tools
import random
from Crypto import Random
from Crypto.Cipher import AES

key = Random.new().read(AES.block_size)

def randomEncrypt():
    with open('task1_source.txt') as file:
        data = [tools.HextoASCII(tools.toHex(line.strip()))for line in file.readlines()]
    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = encryptor.encrypt(tools.pkcs7(data[random.randint(1, 100) % 11], AES.block_size))
    return cipher_text, iv

def getCipherTextAndDecrypt(cipher_text, iv):
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    plain_text = decryptor.decrypt(cipher_text)
    res = tools.pkcs7_check(plain_text)
    if res != None:
        return True
    else:
        return False


def brut_n_block(blocks, iv, numb):
    try:
        brut_block = b''
        for padding in range(1, 17):
            for byte in range(256):
                rand_block = Random.new().read(16 - padding) + bytes.fromhex(hex(byte)[2:].zfill(2)) + tools.xor_blocks(brut_block, bytes.fromhex(hex(padding)[2:].zfill(2)) * (padding - 1))

                attack_text = rand_block + blocks[-numb]

                if getCipherTextAndDecrypt(attack_text, iv):
                    brut_block = bytes.fromhex(hex(padding ^ byte)[2:].zfill(2)) + brut_block
                    break

        if numb == len(blocks):
            return tools.xor_blocks(brut_block, iv)
        else:
            return tools.xor_blocks(brut_block, blocks[-numb-1])
    except TypeError:
        return b''





for tt in range(1000):
    res = []
    encrypted, iv = randomEncrypt()
    blocks = tools.splitBlocks(encrypted, AES.block_size)
    for i in range(0, len(blocks)+1):
        bruted = brut_n_block(blocks, iv, i)
        if bruted == b'':
            break
        res.append(bruted)

    res.reverse()
    if len(res) > 1:
        print(b''.join(res[:-1]))