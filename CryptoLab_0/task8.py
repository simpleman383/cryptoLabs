def task8_demo():

    with open("detectEcb.txt", "r") as file:
        strings = file.readlines()
    strings = [x.strip() for x in strings]

    print(strings)

    for item in strings:
        if detectECB(item):
            print("Success! ECB is detected!", item)


def detectECB(item):
    item = str(item)

    splited_byte_blocks = []
    index = 0
    while index < len(item):
        block = item[index: index + 32]
        splited_byte_blocks.append(block)
        index = index + 32

    for block in splited_byte_blocks:
        n = item.count(block)
        if n > 1:
            return True

    return False