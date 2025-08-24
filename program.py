#File Read & Write Challenge 🖋️:
#Create a program that reads a file and writes a modified version to a new file.
file = open('File.txt', 'r')
content = file.read()
file.close()

file = open('newFile.txt', 'w')
file.write("This file is a modified version of File.txt.\n")
data = content.upper()
file.write(data)
file.close()

#Error Handling Lab 🧪: 
#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
fileName = input("Enter a file name: ")
try:
    file = open(fileName , 'r')
    output = file.read()
    print(f"File content:\n{output}")
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to read this file.")