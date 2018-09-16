
# A module is a Python object with arbitrarily named attributes that you can bind and reference.
# Module allows your code to be  logically organized

# A python module named 'sample' resieds in a file name 'sample.py'
# Python Modules and Libraries are installed by default but they're limited
# Third party modules and libraries are referred to as Packages

# Commonly called as Python Libraries
# Module - Python Script that you can import
# Library - Collection of Python Scripts
# Package - Third party libraries

# You can import a module in another python code file
# Note: It is not a good practice to load everything into memory when Python loads

import math
import os

from datetime import timezone  # from <module> import <func / attribute>
from http import server # Here, html is a Library. It is a folder with group of py files

math_Modules = dir(math)
print('type(dir(math)) is ', type(math_Modules))
print()
print('dir(math) has the following', math_Modules)
print()
print('os.__file__ gives you the path where module is installed', os.__file__)

# Packages
# Package is a hierarchial directory structure that consists of modules, subpackages

# Namespace and Scope

# Variables are names (identifiers) that map to objects.
# A namespace is a dictionary of variable names (keys) and their corresponding objects (values).
# A Python statement can access variables in a local namespace and in the global namespace.
# If a local and a global variable have the same name, the local variable shadows the global variable.

# Each function has its own local namespace. Class methods follow the same scoping rule as ordinary functions.

# Python makes educated guesses on whether variables are local or global.
# It assumes that any variable assigned a value in a function is local.
# Therefore, in order to assign a value to a global variable within a function, you must first use the global statement.

# The statement global VarName tells Python that VarName is a global variable.
# Python stops searching the local namespace for the variable.

# For example, we define a variable Money in the global namespace.
# Within the function Money, we assign Money a value, therefore Python assumes Money as a local variable.
# However, we accessed the value of the local variable Money before setting it, so an UnboundLocalError is the result.
# Uncommenting the global statement fixes the problem


Money = 2000


def AddMoney():
    # Comment the following line to see the error:
    global Money
    Money = Money + 1000


print('Money is ', Money)
AddMoney()
print('Money is ', Money)

# The globals() and locals() function

# If locals() is called from within a function, it will return all the names that can be accessed locally from that function.
# If globals() is called from within a function, it will return all the names that can be accessed globally from that function.
# The return type of both these functions is dictionary. Therefore, names can be extracted using the keys() function.