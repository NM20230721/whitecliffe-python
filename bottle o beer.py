def removeBottle(bottle):
    bottle = bottle - 1
    return bottle

def printBottle(x):
    print(x ,"bottles of beer on the wall,", x, "bottles of beer.", end="")
    x = removeBottle(x)
    print("Take one down, pass it around", x ,"bottles of beer on the wall" )
    return x

totalBottles = 99
for i in range(99):
    totalBottles = printBottle(totalBottles)
