
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

fileObj = open(os.path.join(os.getcwd(),'assets/sample-file.txt'), 'r+')
fileBuffer = open(os.path.join(os.getcwd(),'assets/sample-file-buffer.txt'), 'r+', 1)
fileToWrite = open(os.path.join(os.getcwd(),'assets/sample-file-to-write.txt'), 'w+')

# Accessing a file Object
for line in fileObj.readlines():
    print(line)
    fileToWrite.write(line)

fileObj.close()
fileBuffer.close()
fileToWrite.close()

# The "with" Context Manager
# 
# Both the below blocks serve the same purpose
# Yet, Block using the With Context manager is more preferred than the standard way
# Context manager takes care of closing the file automatically
# 
# Using the With context manager can avoid a problem where an exception may arise,
# before file object is closed and leave your file in open mode by Python which can cause problems

file1 = open("../assets/sample-test.txt", "w")
file1.write("Test")
# Code where exception may arise
file1.write("Test End")
file1.close()

with open("../assets/sample-test.txt","w") as file2 :
    file2.write("Test")
    # Code where exception may arise
    file2.write("Test End")


# Renaming a file
print('Current Working Dir is ', os.getcwd())
if os.path.isfile('../assets/sample-file-written.txt'):
    os.remove('../assets/sample-file-written.txt')
    os.rename(fileToWrite.name, '../assets/sample-file-written.txt')
else:
    os.rename(fileToWrite.name, '../assets/sample-file-written.txt')
    os.remove('../assets/sample-file-written.txt')