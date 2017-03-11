def Buffer_XOR(buffer1, buffer2):

    if len(buffer1) != len(buffer2):
        print("Error: buffer lengths are not equal")
        return None
    elif len(buffer1) % 2 != 0 or len(buffer2) % 2 != 0 :
        print("Error: buffer lengths are odd")
        return None

    result = ""

    bytes1 = []
    index = 0
    while index < len(buffer1):
        hex_block = buffer1[index: index + 2]
        bytes1.append(hex_block)
        index = index + 2

    bytes2 = []
    index = 0
    while index < len(buffer2):
        hex_block = buffer2[index: index + 2]
        bytes2.append(hex_block)
        index = index + 2

    for item1, item2 in zip(buffer1, buffer2):
        byte_xor_result = hex(int(item1, 16) ^ int(item2, 16))[2:]
        result+=byte_xor_result

    return result


  #  8f29336f5e9af0919634f474d248addaf89f6e1f533752f52de2dae0ec3185f818c0892fdc873a69
  #  bf7962a3c4e6313b134229e31c0219767ff59b88584a303010ab83650a3b1763e5b314c2f1e2f166



def task2_demo():
    print("buffer1:")
    buf1 = "8f29336f5e9af0919634f474d248addaf89f6e1f533752f52de2dae0ec3185f818c0892fdc873a69"
    print(buf1)

    print("buffer2:")
    buf2 = "bf7962a3c4e6313b134229e31c0219767ff59b88584a303010ab83650a3b1763e5b314c2f1e2f166"
    print(buf2)

    print("Excpected result:")
    print("305051cc9a7cc1aa8576dd97ce4ab4ac876af5970b7d62c53d495985e60a929bfd739ded2d65cb0f")

    print("Result:")
    print(Buffer_XOR(buf1,buf2))