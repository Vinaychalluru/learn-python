# Question 25
# Level 1

# Question:
# Define a class, which have a class parameter and have a same instance parameter.


class MyClass:
    'A Class'
    myID = 1

    def __init__(self, myID=None):
        self.myID = myID

    def __del__(self):
        pass


cObj = MyClass(100)
print("Class ID is %d Instance ID is %d" % (MyClass.myID, cObj.myID))

cObj1 = MyClass()
cObj1.myID = 200
print("Class ID is %d Instance ID is %d" % (MyClass.myID, cObj1.myID))
