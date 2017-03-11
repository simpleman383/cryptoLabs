import task2
import hex_base64_converter
import re


def getBytes(hex_buffer):
    hex_buffer = str(hex_buffer)
    cipher_bytes = []
    index = 0
    while index < len(hex_buffer):
        hex_block = hex_buffer[index: index + 2]
        cipher_bytes.append(hex_block)
        index = index + 2
    return cipher_bytes


def decrypt(cipher_text, key):
    decrypted_byte_code = task2.Buffer_XOR(cipher_text,key)
    decrypted_text = ""

    splited_byte_blocks = []
    index = 0
    while index < len(decrypted_byte_code):
        hex_block = decrypted_byte_code[index: index + 2]
        splited_byte_blocks.append(hex_block)
        index = index + 2

    for byte in splited_byte_blocks:
        decrypted_text += chr(int(byte, 16))

    return decrypted_text


def brutXor(cipher_text):
    all_texts = []

    for char_code in range(256):

        generate_byte = hex(char_code)[2:]
        if char_code < 16:
            generate_byte = "0" + generate_byte
        all_texts.append(decrypt(cipher_text, generate_byte * (len(cipher_text) // 2)))

    ttt = filterNonLetter(all_texts)
    if ttt:
        f = open('breakRepeatedKeyXor-key.txt', 'a')
        f.write(chr(all_texts.index(ttt[0])))
        f.close()
    return ttt


def printable(text):
    text = str(text).lower()
    eng_text_symb = "abcdefghijklmnopqrstuvwxyz0123456789+-*/ \n!?()=<>.,'\":"
    for char in text:
        if eng_text_symb.count(char) == 0:
            return False
    return True


def filterNonLetter(all_texts):
    result = []
    for text in all_texts:
        if printable(text):
            result.append(text)
    return result


def combineDecryptedLines(decrypted_lines_list):
    decrypted_text = ""
    index_of_line = 0
    index_of_char = 0

    if decrypted_lines_list:
        while index_of_char < len(decrypted_lines_list[index_of_line]):

            decrypted_text += decrypted_lines_list[index_of_line][index_of_char]

            if index_of_line == len(decrypted_lines_list) - 1:
                index_of_char += 1

            index_of_line = (index_of_line + 1) % len(decrypted_lines_list)

        return decrypted_text
    else:
        return ""



def task6_demo():
    with open("breakRepeatedKeyXor.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    cipher_base64 = ""
    for line in content:
        cipher_base64 += line

    cipher_hex = hex_base64_converter.toHex(cipher_base64)
    print(cipher_hex)

    cipher_bytes = getBytes(cipher_hex)
    print(cipher_bytes)

    for key_length in range(2,40):

        print("Trying key length = ", key_length)

        splitted_lines = []

        for i in range(key_length):
            index = i
            line = ""
            while index < len(cipher_bytes):
                line += cipher_bytes[index]
                index+=key_length
            splitted_lines.append(line)

        #print(splitted_lines)
        decrypted_lines_list = []

        for line in splitted_lines:
            decrypted = brutXor(line)
            print(decrypted)
            if not decrypted:
                break
            else:
                decrypted_lines_list.append(decrypted[0])


        print("SOURCE TEXT")
        if decrypted_lines_list:
            print(combineDecryptedLines(decrypted_lines_list))
        else:
            print("NOT FOUND")
