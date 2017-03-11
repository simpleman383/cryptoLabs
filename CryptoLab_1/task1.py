def toHex(string):
    string = str(string)
    res = ""
    for char in string:
        res += hex(ord(char))[2:].zfill(2)
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
    if string.endswith(ord(end_byte.decode()) * end_byte):
        print("PKCS7_CHECK: TRUE")
        return string[:-1 * ord(end_byte.decode())]
    else:
        print("PKCS7_CHECK: FALSE")
        return None


padded = pkcs7("YELLOW SUBMARINE", 16)
print("PADDED_STRING: ", padded)

bad_string = b'YELLOW_SUBMARINE\x03'

unpadded = pkcs7_check(b'12345678901234\x01\x01')
print("UNPADDED_STRING: ",unpadded)

unpadded = pkcs7_check(bad_string)
print("UNPADDED_STRING: ",unpadded)