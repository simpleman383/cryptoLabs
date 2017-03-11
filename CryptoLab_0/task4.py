import task3

def task4_demo():

    with open("detectSingleXor14") as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print(content)

    counter = 1
    for line in content:
        print("Line ", counter)
        task3.task3_demo(line)
        counter += 1
