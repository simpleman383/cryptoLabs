def toBase64(hex_string):
    #hex_string = "faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0"
    bin_string = ""

    # проверяем исходную строку в hex
    if len(hex_string) % 2 != 0:
        print("Error: Hex-string length is odd")
        return None

    hex_chars = "ABCDEF0123456789abcdef"
    for i in hex_string:
        if hex_chars.count(i) == 0:
            print("error")
            return None

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    dict = {index: alphabet[index] for index in range(64)}

    #разделяем на байты
    splited_hex_blocks = []
    index = 0
    while index < len(hex_string):
        hex_block = hex_string[index: index + 2]
        splited_hex_blocks.append(hex_block)
        index = index + 2

    # превращаем в бинарную строку
    for item in splited_hex_blocks:
        bin_string = bin_string + str(bin(int("0x" + item, 16)))[2:].zfill(8)

    # делим на блоки по 6 бит
    splited_bin_blocks = []
    index = 0
    while index < len(bin_string):
        bin_block = bin_string[index: index + 6]
        if (len(bin_block) < 6):
            bin_block = bin_block + "0" * (6 - len(bin_block))
        splited_bin_blocks.append(bin_block)
        index = index + 6

    # собираем строку в base64
    str_base64 = ""
    for item in splited_bin_blocks:
        str_base64 = str_base64 + dict.get(int("0b" + item, 2))

    # добавляем спец суффикс в зависимости от кратности
    if (len(hex_string) / 2) % 3 == 1:
        str_base64 = str_base64 + 2 * "="
    elif (len(hex_string) / 2) % 3 == 2:
        str_base64 = str_base64 + 1 * "="

    return str_base64


def toHex(base64_string):


    hex_string = ""
    if len(base64_string) % 4 != 0:
        print("Error: base64 must be 4N bytes")
        return None

    if base64_string.count('=') > 2 or str(base64_string).rstrip('=').count('=') != 0 :
        print('format error')
        return None



    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    dict = {alphabet[index]: index for index in range(64)}

    # делим на блоки по 4 байта
    blocks = []
    index = 0
    while index < len(base64_string):
        hex_block = base64_string[index: index + 4]
        blocks.append(hex_block)
        index = index + 4

    # дешифруем каждый блок
    for item in blocks:
        #  переводим блок в бинарную строку
        bin_string = ""
        for char in item:
            if dict.get(char) != None:
                base64_ord_bin = str(bin(dict.get(char)))[2:]
                base64_ord_bin = (6 - len(base64_ord_bin)) * "0" + base64_ord_bin
                bin_string = bin_string + base64_ord_bin

        # учитываем спец суффикс, чтобы избавиться от лишних битов
        suffix_counter = item.count("=")
        bin_string = bin_string[0:len(bin_string) - 2 * suffix_counter]

        # делим на блоки по 8 бит
        splited_bin_blocks = []
        index = 0
        while index < len(bin_string):
            bin_block = bin_string[index: index + 8]
            splited_bin_blocks.append(bin_block)
            index = index + 8

        # собираем hex строку
        for item in splited_bin_blocks:
            byte = int(item, 2)
            if byte < 16:
                hex_string = hex_string + "0" + str(hex(int(item, 2)))[2:]
            else:
                hex_string = hex_string + str(hex(int(item, 2)))[2:]

    return hex_string


def ASCIItoHex(string):
    string = str(string)
    res = ""
    for char in string:
        res += hex(ord(char))[2:].zfill(2)
    return res

def HextoASCII(hex_string):
    res = ''
    for ch in range(0, len(hex_string), 2):
        res += chr(int(hex_string[ch: ch+2], 16))
    return res

def pkcs7(string, size):
    if (size <= 0 or size > 127):
        print("error: size")
        return None
    string = str(string)
    result = string[:]
    while len(string) > size:
        string = string[size:]
    byteToAdd = hex(size)[2:].zfill(2) if size == len(string) or len(string) == 0 else hex(size - len(string))[2:].zfill(2)
    return (result + int('0x' + byteToAdd, 16) * chr(int('0x' + byteToAdd,16))).encode()


def pkcs7_check(string):
    end_byte = string[-1:]
    try:
        if string.endswith(ord(end_byte.decode()) * end_byte):
            #print("PKCS7_CHECK: TRUE")
            return string[:-1 * ord(end_byte.decode())]
        else:
            #print("PKCS7_CHECK: FALSE")
            return None
    except UnicodeError:
        #print("PKCS7_CHECK: FALSE")
        return None

def splitBlocks(text, block_size):
    blocks = []
    for i in range(0, len(text), block_size):
        blocks.append(text[i:i + block_size])
    return blocks


def xor_blocks(block1, block2):
    if len(block1) != len(block2):
        return None
    if len(block1) == 0 or len(block2)==0:
        return b''
    else:
        res = b''
        for b1,b2 in zip(block1, block2):
            res += bytes.fromhex(hex(b1 ^ b2)[2:].zfill(2))
        return res