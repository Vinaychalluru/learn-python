# Python deletes unneeded objects (built in types and class instances) automatically to free memory space
# Garbage Collector runs during program execution and is trigerred when an object's reference count reaches zero
# An object's reference count decreases when
# it's deleted with del, its ref is reassigned or the ref goes out of scope

# You normally will not notice when the garbage collector destroys an orphaned instance and reclaims its space.
# But a class can implement the special method __del__(), called a destructor,
# that is invoked when the instance is about to be destroyed.
# This method might be used to clean up any non memory resources used by an instance


class Point:
    'Class that holds the x,y coordinates of the point'
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print('I am the initializer for class Point')

    def __del__(self):
        class_name = self.__class__.__name__
        print('Destoying instance of %s' % class_name)


pt1 = Point()
pt4 = pt3 = pt2 = pt1

print('%d ; %d ; %d ; %d ' % (id(pt1), id(pt2), id(pt3), id(pt4)))

del pt1
del pt2
del pt3
del pt4
