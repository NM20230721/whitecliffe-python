alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z", " "]

inputEncrypt = input("What sentence do you want to encrypt?")
shift = int(input("How many shifts? "))
inputSize = len(inputEncrypt)
encryptText = ""


for i in range(len(alphabet)+shift):
    x = alphabet.pop()
    alphabet.insert(0, x)



for i in range(inputSize):
    for x in range(len(alphabet)):
        if inputEncrypt[i] == alphabet[x]:
            add = alphabet[x-shift]
    encryptText = encryptText + add

print(encryptText)