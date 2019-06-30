import traceback
import random
import math


class Sorting(object):
    """I am Sorting Class
    """

    def selection_Sort(self, arr):
        l = len(arr)
        for i in range(l):
            min_idx = i
            for j in range(i + 1, l):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
        return arr

    def bubble_Sort(self, arr):
        l = len(arr)
        # The function always runs O(n^2) time even if the array is sorted
        # It can be optimized by stopping the algorithm if inner loop didn’t cause any swap
        for i in range(l):
            swap_flag = False
            for j in range(l - 1 - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_flag = True
            if swap_flag == False:
                break

    def insertion_Sort(self, arr):
        pass

    def merge_Sort(self, arr):
        if len(arr) < 2:
            return
        else:
            l = len(arr)

        m = l // 2
        l_arr = arr[:m]
        r_arr = arr[m:]
        self.merge_Sort(l_arr)
        self.merge_Sort(r_arr)

        i = j = k = 0

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                i = i + 1
            else:
                arr[k] = r_arr[j]
                j = j + 1
            k = k + 1

        while i < len(l_arr):
            arr[k] = l_arr[i]
            i = i + 1
            k = k + 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j = j + 1
            k = k + 1

    def heap_Sort(self, arr):
        pass
    
    def quick_Sort(self, arr):
        pass



try:
    s = Sorting()
    unsorted_arr = [7, 4, 5, 6, 22435, 2357, 3, 6, 843, 2, 1]
    s.selection_Sort(unsorted_arr)
    print(unsorted_arr)
    unsorted_arr = [7, 4, 5, 6, 22435, 2357, 3, 6, 843, 2, 1]
    s.bubble_Sort(unsorted_arr)
    print(unsorted_arr)
    unsorted_arr = [7, 4, 5, 6, 22435, 2357, 3, 6, 843, 2, 1]
    s.insertion_Sort(unsorted_arr)
    print(unsorted_arr)
    unsorted_arr = [7, 4, 5, 6, 22435, 2357, 3, 6, 843, 2, 1]
    s.merge_Sort(unsorted_arr)
    print(unsorted_arr)

except Exception as e:
    print("Encountered Exception:", repr(e))
    traceback.print_exc()
    pass
