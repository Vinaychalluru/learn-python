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
    # and those attributes are not be directly visible to outsiders.
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
