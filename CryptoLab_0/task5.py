import task2

def task5_demo():
    text = "Never trouble about trouble until trouble troubles you!"
    key = "ICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEI"

    result = ""
    for ind1,ind2 in zip(text,key):
        result += hex(ord(ind1) ^ ord(ind2))[2:]

    print(result)