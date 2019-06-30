import traceback
import random
import math


class Search(object):
    """I am Search class
    I have methods for Searching an element in a list
    and I implement various approaches to do so"""
    searches_made = 0

    def __init__(self):
        """I am the Constructor for Search"""
        Search.searches_made = Search.searches_made + 1
        pass

    def linear_Search(self, x, elements):
        """
        type x : int \n
        type elements : list \n
        rtype idx : int"""
        for i, e in enumerate(elements):
            if x == e:
                return i
        else:
            return -1
        pass

    def binary_Search(self, x, elements):
        """ binary_Search() """
        elements.sort()
        l, r = 0, len(elements) - 1
        while r >= l:
            m = l + (r - l) // 2
            if x == elements[m]:
                return m
            elif x > elements[m]:
                l = m + 1
            elif x < elements[m]:
                r = m - 1
        else:
            return -1

    def jump_Search(self, x, elements):
        elements.sort()
        m = int(math.sqrt(len(elements)))
        l, r = 0, len(elements) - 1
        p = l + m
        while l < r:
            if x > elements[p]:
                l, p = p, p + m
                if p > r:
                    p = r
            elif x < elements[p]:
                if x < elements[l]:
                    return -1
                for i, e in enumerate(elements[l:p]):
                    if x == e:
                        return i + l
                else:
                    return -1
            else:
                return p
        else:
            return -1

    def interpolation_Search(self, x, elements):
        elements.sort()
        l, r = 0, len(elements) - 1
        while r >= l and x >= elements[l] and x <= elements[r]:
            if r == l:
                if elements[l] == x:
                    return l
                return -1
            m = l + ((x - elements[l]) * (r - l) //
                     (elements[r] - elements[l]))
            if x == elements[m]:
                return m
            elif x > elements[m]:
                l = m + 1
            elif x < elements[m]:
                r = m - 1
        else:
            return -1

    def exponential_Search(self, x, elements):
        elements.sort()
        e = 1
        l, r = 0, len(elements) - 1

        if x < elements[l] or x > elements[r]:
            return -1

        while e < r and elements[e] <= x:
            e = e * 2

        l = e // 2
        r = min(e, r)

        return self.binary_Search(x, elements[l:r])

    def ternary_Search(self, x, elements):
        elements.sort()
        l, r = 0, len(elements) - 1
        while r >= l :
            mid1 = l + (r - l) // 3
            mid2 = mid1 + (r - l) //3
            if x == elements[mid1]:
                return mid1
            
            if x == elements[mid2]:
                return mid2

            if x < elements[mid1]:
                r = mid1 - 1
            elif x > elements[mid2]:
                l = mid2 + 1
            else:
                l = mid1 + 1
                r = mid2 - 1
        else:
            return -1
        pass


# Main implementation of Searching
try:
    num_to_find = [1, 2, 7, 3434, 64545, 50, 0, -
                   20, -30, -1, 10, 2323, 5452323, 455, 333]
    x = random.choice(num_to_find)

    s = Search()
    rc = s.linear_Search(x, range(10))
    rc = s.binary_Search(
        x, [1, 5, 10, 50, 100, 2, 4, 3, 6, 9])
    rc = s.jump_Search(x, [1, 5, 10, 50, 100, 2, 4, 3, 6, 9])
    # rc = s.jump_Search(x, list(range(10000,7000000)))
    rc = s.interpolation_Search(x, list(range(90, 500, 3)))
    rc = s.exponential_Search(x, list(range(0, 100000, 5)))
    if rc != -1:
        print("Found  %d at index : %d" % (x, rc))
    else:
        print("%d not found" % (x))
    pass
except Exception as e:
    print("Encountered an exception : " + repr(e))
    traceback.print_exc()
else:
    pass
finally:
    pass
