import task2
import re

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


def filterNonLetter(all_texts):
    result = []
    regexp = re.compile("[\n.,+-/*()!?\"':\[\]%^]")
    for text in all_texts:
        text = re.sub(regexp,"",text)
        if str(text).replace(" ", "").isalpha() and re.match("[A-Za-z0-9]",text):
            result.append(text)
    return result


def getCharFreq(text):
    text = str(text).lower().replace(" ","")
    table = {}
    letters = {text[i] for i in range(len(text))}
    for item in letters:
        freq = text.count(item)/len(text) * 100
        table[item] = freq
    return table



def calculateError(text_freq, eng_freq):
    error = 0.0
    keys = dict(text_freq).keys()
    for k in keys:
        error += abs(dict(text_freq).get(k) - dict(eng_freq).get(k))
    return error


def filterEnglishText(all_texts):

    if not all_texts:
        print("Error: no text")
        return ""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    table_freq = {alphabet[i] : freq[i] for i in range(26)}

    min_error = calculateError(getCharFreq(all_texts[0]), table_freq)
    eng_text = all_texts[0]

    for text in all_texts:
        current_text_table_freq = getCharFreq(text)
        err = calculateError(current_text_table_freq, table_freq)
        if err < min_error:
            eng_text = text

    return eng_text


def task3_demo(cipher_text):

    all_texts = []

    pairs = {}


    for char_code in range(256):

        generate_byte = hex(char_code)[2:]
        if char_code < 16:
            generate_byte = "0" + generate_byte
        pairs[decrypt(cipher_text, generate_byte*(len(cipher_text) // 2))] = char_code
        all_texts.append(decrypt(cipher_text, generate_byte*(len(cipher_text) // 2)))


    ttt = filterNonLetter(all_texts)

        #f = open('key.txt', 'a')
        #f.write(chr(all_texts.index(ttt[0])))
        #f.close()


    ttt = filterEnglishText(ttt)
    print(ttt)
    #print(all_texts)

    return ttt
    #041811045013111e5003110615501815025000151f001c1550111e1450021503041f0215
