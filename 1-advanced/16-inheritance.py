class Shape:
    'I am the Parent class called Shape'
    parent_attr = 100

    def __init__(self):
        print('I am the %s Initializer' % self.__class__.__name__)

    def __del__(self):
        print('Destroying instance of %s' % self.__class__.__name__)

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
except Exception as e:
    print('Encountered an exception : ' + repr(e))
