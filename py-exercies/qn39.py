# Question 39
# Level 2

# Question:
# Define a class named American which has a static method called printNationality.
# Define a class named American and its subclass NewYorker. 


class American:
    'I am Class American'

    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def printNationality():
        print('Nationality - American')


class Newyorker(American):
    '''I am a sub class for the Class American'''

    def __init__(self):
        pass

    def __del__(self):
        pass


American.printNationality()
Newyorker.printNationality()
