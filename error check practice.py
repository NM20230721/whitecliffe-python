""""
Up to $14,000	                10.5% ==== Bracket A
Over $14,000 and up to $48,000	17.5% === Bracket B
Over $48,000 and up to $70,000	30% === Bracket C
Over $70,000 and up to $180,000	33% === Bracket D
Remaining income over $180,000	39% === Bracket E
"""

def Bracket_A(x):
    x = x * 0.105
    return x

def Bracket_B(x):
    x = (x - 14000) * 0.175
    x = x + 1470
    return x

def Bracket_C(x):
    x = (x - 48000) * 0.30
    x = x + 7420
    return x

def Bracket_D(x):
    x = (x - 70000) * 0.33
    x = x + 14020
    return x

def Bracket_E(x):
    x = (x - 180000) * 0.39
    x = x + 50320
    return x



while 1 == 1:
    income = (input("How much money do you make in a year: "))
    try:
        income = int(income)
        if type(income) is int:
            break
    except ValueError:
        print("Only integers are allowed")

tax = 0
if income <= 14000:
    tax = Bracket_A(income)
elif 48000 >= income > 14000:
    tax = Bracket_B(income)
elif 70000 >= income > 48000:
    tax =Bracket_C(income)
elif 180000 >= income > 70000:
    tax = Bracket_D(income)
else:
    tax = Bracket_E(income)

print("The total tax is:", tax)