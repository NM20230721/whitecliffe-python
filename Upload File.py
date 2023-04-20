text = open("mytext.txt", "r")
print(text.readline())

print("---------------------------")
print("WELCOME TO TEXT WRITER")

newText = input("Input your text: ")
nameFile = input("Name of file: ")
nameFile = nameFile + ".txt"

newFile = open(nameFile, "x")
newFile.write(newText)
newFile.close()
newFile = open(nameFile, "r")

print(newFile.read())
newFile.close()