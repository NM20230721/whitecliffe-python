def challenge1(name, number):
    print("hello there, my name is", name, "and my number is", number)

challenge1(input("challenge 2 input name: "), input("challenge 1 input number: "))


def challenge2(num):
    for i in range(4):
        multiple = num*(i+1)
        print(multiple)

challenge2(int(input("Challenge 2 input: ")))


def challenge3(x,y):
    for i in range(y):
        multiple = x * (i+1)
        print(multiple)

challenge3(int(input("challenge 3 input x: ")), int(input("challenge 3 input y: ")))