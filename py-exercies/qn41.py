# Question 41

# Question:
# Define a custom exception class which takes a string message as attribute.


import traceback


class CustomExcptn(Exception):
    '''A Custom Exception Class'''

    def __init__(self, message):
        self.exception_message = message

    def __del__(self):
        pass


try:
    print('Example for a Custom Exception Class')
    raise CustomExcptn('A custom exception')
except CustomExcptn as e:
    print('Encountered an exception - ' + repr(e))
    traceback.print_exc()
