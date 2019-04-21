# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

import traceback

arr = [x**2 for x in range(1, 15)]
s = int(input("Enter the search element : "))


def find_ele(left, right):
    global s
    global arr
    if right >= left:
        # Observe how position is defined
        pos = left + (right - left)//2
        if s > arr[pos]:
            return find_ele(pos + 1, right)
        elif s < arr[pos]:
            return find_ele(left, pos - 1)
        elif s == arr[pos]:
            return pos
    else:
        return -1


try:
    result = find_ele(0, len(arr) - 1)

    if result != -1:
        print('Element found at the position :', result)
    else:
        print('Element is not present')

except Exception as e:
    print('Encountered an exception', repr(e))
    traceback.print_exc()
