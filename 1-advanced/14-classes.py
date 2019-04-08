class Employee:
    'I am the Employee class'
    instance_Count = 0

    def __init__(self, id, name):
        # I am Employee class constructor or initialize method
        # I am called when Employee class is instantiated
        Employee.instance_Count = Employee.instance_Count + 1
        self.id = id
        self.name = name

    def getDetails(self):
        print('Emp ID - %d' % self.id)
        print('Emp Name - %s' % self.name)


try:
    emp1 = Employee(100, 'Alpha')
    emp2 = Employee(200, 'Beta')
    emp3 = Employee(300, 'Charlie')

    emp1.getDetails()

    # I can add a new attriubute like below
    emp1.age = 15
    emp1.__setattr__('Location', 'India')
    print('emp1 Location - %s' % emp1.__getattribute__('Location'))
    print('emp1 has attr age - %s' % hasattr(emp1, 'age'))
    emp1.__delattr__('age')

    emp2.getDetails()
    emp2.__setattr__('age', 50)
    print('emp2 age is - %d' % emp2.__getattribute__('age'))

    print('Total no of Employee instances - %d' % Employee.instance_Count)

    print('Employee.__doc__ - %s' % Employee.__doc__)
    print('Employee.__module__ - %s' % Employee.__module__)
    print('Employee.__bases__ - %s' % Employee.__bases__)
    print('Employee.__dict__ - %s' % Employee.__dict__)

    print('emp3 has no age. Trying to access raises an exception' + emp3.age)

except Exception as e:
    print('Encountered an Exception : ' + repr(e))
