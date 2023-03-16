
print("Welcome!!!!")

def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(5,2)

def sub_numbers(num1, num2):
    print(num1 - num2)
sub_numbers(5,2)


def name(first, last):
    print(first, last)
name ("John","Doe")

def repeater(theString, num):
    for i in range(num):
        print(theString)
x = int(input("Your value?"))
y = str(input("Your string?"))
repeater(y,x)

def sum(list):
    total = 0
    for i in list:
        total = total + i
    print("The sum:", total)

myList = [5,2,3,4]
sum(myList)


def multiply(list):
    sum = 1
    for i in list:
        sum = sum * i
    print("All of the numbers multiplied is ", sum)
myList2 = [5,5,2,4]
multiply(myList2)
