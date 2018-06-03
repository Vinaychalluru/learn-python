# Comment mush have a blank space after hashTag - Per PEP8

# Indentation must be followed rigidly
if True:
    print("True")
else:
    print("False")

# Triple Quotes - used to span the string across multiple lines
word = 'word'
sentence = 'This is a sentence'
paragraph = '''This is a paragraph. It is
made up of multiple lines and sentences.'''

# User input

# Semicolon allows multiple statements on a single line sa below comment
# Per standard, it is not recommended
# import sys ; var="test" ; sys.stdout.write("My var is " + var)
import sys
var = "test"
sys.stdout.write("My var is " + var)

# Suites - A group of individual statements, which make a single code block are called suites in Python
if True:  # Header line of the Suite
    print(" if ")
elif 10 > 100:
    print("elif")
else:
    print("else")

# VS Code can fold or unfold the regions. Try Ctrl + Shift + [ / Ctrl + Shift + ]
# region # Code block start

print(sentence.capitalize())
print(sentence.split())

# endregion # Code block end

# In Python, Packages are how you obtain any number of useful code libraries,
# typically from PyPi

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot
