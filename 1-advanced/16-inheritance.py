class Shape:
    'I am the Parent class called Shape'
    parent_attr = 100

    def __init__(self):
        print('I am the %s Initializer' % self.__class__.__name__)

    def __del__(self):
        print('Destroying instance of %s' % self.__class__.__name__)

    def __str__(self):
        return f"{Shape.__name__}"

    def setAttr(self, attr):
        Shape.parent_attr = attr

    def getAttr(self):
        print('Attr : %d' % Shape.parent_attr)

    def printColor(self):
        print('%s can have any color' % self.__class__.__name__)


# class Child(Parent)
# class Child(Parent1, Parent2)
class Square(Shape):
    'I am a Square Shape'

    def __init__(self):
        print('I am the %s Initializer' % self.__class__.__name__)
        pass

    def __del__(self):
        print('Destroying instance of %s' % self.__class__.__name__)

    def printArea(self):
        print('Area of a %s is length * length' % self.__class__.__name__)
        pass


class Parent1(object):
    """Parent1"""

    def __init__(self):
        self.p1_age = 1

    def getAge(self):
        print(f"Parent1 getAge is accessed. My Age is {self.p1_age}")
        return f"Parent1 age is {self.p1_age}"


class Parent2(object):
    """Parent2"""

    def __init__(self):
        self.p2_age = 2

    def getAge(self):
        return f"Parent2 age is {self.p2_age}"


class Child12(Parent1, Parent2):
    """Child12 - Inherits from Parent1 and Parent2"""

    def __init__(self):
        self.c_age = 12
        # The program throws error if the below line is commented
        # The Super class’s attributes would not be initialized; 
        # You have to explicitly call the __init__() of the super classes from their respective sub classes
        super().__init__()

class SuperClass:  # Super Class for SubClass1 SubClass2 & SubSubClass
    def __init__(self, pParamSuper):
        print('SuperClass.__init__')
        self.superValue = pParamSuper

    def getSuperAttr(self):
        print('SuperClass: We are inside getSuperAttr.', self.superValue)


class SubClass1(SuperClass):  # Inherits SuperClass
    def __init__(self, pParamSubCls1, pParamSubCls2, pParamSupCls):
        print('SubClass1.__init__')
        self.sub1Value = pParamSubCls1
        super().__init__(pParamSubCls2, pParamSupCls)

    def getSub1Attr(self):
        print('SubClass1: We are inside getSub1Attr.', self.sub1Value)


class SubClass2(SuperClass):  # Inherits SuperClass
    def __init__(self, pParamSubCls2, pParamSupCls):
        print('SubClass2.__init__')
        self.sub2Value = pParamSubCls2
        super().__init__(pParamSupCls)

    def getSub2Attr(self):
        print('SubClass2: We are inside getSub2Attr.', self.sub2Value)


class SubSubClass(SubClass1, SubClass2):  # Inherits both SubClass1 & SubClass2
    def __init__(self, pParam, pParamSubCls1, pParamSubCls2, pParamSupCls):
        print('SubSubClass.__init__')
        self.subSubValue = pParam
        super().__init__(pParamSubCls1, pParamSubCls2, pParamSupCls)

    def getSubSubAttr(self):
        print('SubSubClass: We are inside getSubSubAttr.', self.subSubValue)


def testMultiInheritance():
    objNew = SubSubClass(10, 20, 30, 40)
    objNew.getSubSubAttr()
    objNew.getSub1Attr()
    objNew.getSub2Attr()
    objNew.getSuperAttr()
    # The MRO list of SubSubClass
    # It is Method Resolution Order (MRO), which helps super() functions to makes its decision that which class has to be used
    # It is based on the “C3 Superclass Linearization” algorithm
    # This is called a linearization, because the tree structure is broken down into a linear order
    print('\nMRO list of SubSubClass: ', SubSubClass.mro())
    print(f"\n{objNew.__class__.__name__} base classes are {objNew.__class__.__bases__}")
    print()


try:
    # c = Child()          # instance of Child
    # c.childMethod()      # child calls its method
    # c.parentMethod()     # calls parent's method
    # c.setAttr(200)       # again call parent's method
    # c.getAttr()          # again call parent's method

    shp1 = Shape()
    sqr1 = Square()
    sqr1.printArea()
    sqr1.printColor()
    sqr1.setAttr(200)
    sqr1.getAttr()

    print('issubclass(Square,Shape) : ' + str(issubclass(Square, Shape)))
    print('isinstance(sqr1,Square) : ' + str(isinstance(sqr1, Square)))
    print('isinstance(sqr1,Shape) : ' + str(isinstance(sqr1, Shape)))

    print("")
    c = Child12()
    print(f"{c.__class__.__name__} inherits from {c.__class__.__bases__}")
    print(f"Both the parents have same method getAge()")
    print(f" -- Which Parent's method is made use of ? : MRO of '{c.__class__.__name__}' decides -- ")
    print(f"{Child12.mro()}")
    print(f"c.getAge() gets - {c.getAge()}")

    print("")
    testMultiInheritance()


except Exception as e:
    print('Encountered an exception : ' + repr(e))

else:
    print(" -- No exceptions occurred -- \n")
