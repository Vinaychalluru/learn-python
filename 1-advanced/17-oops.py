# OOPS
#     - Encapsulation    : Bundling of data with methods that operate on them
#     - Data Abstraction : Encapsulation + Hiding
#     - Polymorphism     : 
#     - Inheritance      : Use attributes and methods of another Class - Override / Extend 

# Benefits
#     - Modular structure
#     - Reusability of Objects and methods
#     - Data is safe and secure with Abstraction (Encapsularion + Data Hiding = Abstraction)
#     - Adapt and modify the existing behavior of your Software
#     - Productivity of Programmers / Faster Development
#     - OOP Modles real world entities as Software entities
#     - DRY Concept - Don't Repeart Yourself

# Class and Objects
#     - A Class is the Blueprint
#     - Object is an instance - Created by Instantiation
#     - __init__() / __del__() - Constructor and Destructor for the Object
#     - An object is destroyed when the program terminates or it goes out of the scope
#     - __str__() Returns whatever we want to display when a object itself is printed. Or explicitly convert an Object into a string
#     - Built In Class Attributes : __dict__, __doc__, __name__, __module__,__bases__
#     - You have to explicitly call the __init__() of the Super classes from their respective sub classes

# MRO
#     - MRO : Method Resolution Order
#     - It is MRO that helps super() functions to makes its decision that which class has to be used
#     - It is based on the “C3 Superclass Linearization” algorithm
#     - This is called a linearization, because the tree structure is broken down into a linear order

# Operator Overloading
#     - Allow us to perform arithmetic operations between two Objects

# Polymorphism
#     - Python is implicitly Polymorphic. You can call the same function with various types
#     - Unlike C++ and Java, you cannot use the same function name based on the argument length or order
#     - As the latest version of a function will override the earlier definition

class ComplexNumber:
    def __init__(self, pReal, pImaginary):
        self.real = pReal
        self.imaginary = pImaginary

    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + "i"

    def __add__(self, pNewObj):
        vReal = self.real + pNewObj.real
        vImaginary = self.imaginary + pNewObj.imaginary
        vNewComplexNum = ComplexNumber(vReal, vImaginary)
        return vNewComplexNum

    def __sub__(self, pNewObj):
        vReal = self.real - pNewObj.real
        vImaginary = self.imaginary - pNewObj.imaginary
        vNewComplexNum = ComplexNumber(vReal, vImaginary)
        return vNewComplexNum

    def __truediv__(self, pNewObj):
        return "Division is not supported"

def main():
    vComp1 = ComplexNumber(4, 5)
    vComp2 = ComplexNumber(2, 1)
    print("First Complex Num: ", vComp1)
    print("Second Complex Num: ", vComp2)

    vComp3 = vComp1 + vComp2    # obj3 = obj1.__add__(obj2)
    print("\nSum: ", vComp3)

    vComp4 = vComp1 - vComp2    # obj3 = obj1.__sub__(obj2)
    print("Diff: ", vComp4)

    vComp5 = vComp1 / vComp2    # obj3 = obj1.__truediv__(obj2)
    print("Div: ", vComp5)

main()

class Parent:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def hello(self):
        print('Hello - I am inside Parent %s' % self.__class__.__name__)
    pass


class Child(Parent):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def hello(self):
        print('Hello - I am inside Child %s' % self.__class__.__name__)
    pass


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


class Secret:
    # Name class attributes with a double underscore prefix,
    # and those attributes are not directly visible to outsiders
    __myHiddenVar = 100

    def __init__(self):
        pass

    def __del__(self):
        pass

    def printVar(self):
        print('Var is %d - I am accessible inside the class' % self.__myHiddenVar)

# Base Overloading Methods
# __init__
# __del__
# __repr__
# __str__
# __cmp__


def sum(x, y):
    return x + y


try:
    # Overriding - Inheritance
    child_Obj = Child()
    child_Obj.hello()
    # Operator Overloading
    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
	# __add__ & __str__ are overloaded here
	# To see the difference, comment methods inside the class and see for yourself
    print(v1 + v2)
    # Data Hiding
    s = Secret()
    s.printVar()
    # The variable is hidden. Below line would throw an exception
    print('Var is %d' % s.__myHiddenVar)
except Exception as e:
    print('Encountered an Exception : ' + repr(e))
finally:
    print('Bye')
