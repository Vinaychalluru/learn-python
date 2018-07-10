
import os

# Keyboard Input
# input(prompt)
Name = input('Enter your name : ')
print('Hello %s' % (Name))

# Files
# Open a file before read or write
# Close a file when operations are done
print("Test")
print('Current Working Dir is ', os.getcwd())

fileObj = open('./python-learn/assets/sample-file.txt', 'r+')
fileBuffer = open('./python-learn/assets/sample-file-buffer.txt', 'r+', 1)
fileToWrite = open('./python-learn/assets/sample-file-to-write.txt', 'w+')

# Accessing a file Object
for line in fileObj.readlines():
    print(line)
    fileToWrite.write(line)

fileObj.close()
fileBuffer.close()
fileToWrite.close()


# Renaming a file
print('Current Working Dir is ', os.getcwd())
if os.path.isfile('./python-learn/assets/sample-file-written.txt'):
    os.remove('./python-learn/assets/sample-file-written.txt')
    os.rename(fileToWrite.name, './python-learn/assets/sample-file-written.txt')
else:
    os.rename(fileToWrite.name, './python-learn/assets/sample-file-written.txt')
    os.remove('./python-learn/assets/sample-file-written.txt')