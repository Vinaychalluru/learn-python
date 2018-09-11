# Question 20
# Level 3

# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


class numGen:
    nbr = 0

    def __init__(self):
        pass

    def __del__(self):
        pass

    def iterate(self, nbr):
        self.nbr = nbr
        return [x for x in range(self.nbr) if x % 7 == 0]


ngObj = numGen()
print(ngObj.iterate(70))


def putNumbers(n):
    'generator - yield'
    i = 0
    while i < n:
        j = i
        i = i+1
        if j % 7 == 0:
            yield j


div_7_generator = putNumbers(70)

print(next(div_7_generator))
