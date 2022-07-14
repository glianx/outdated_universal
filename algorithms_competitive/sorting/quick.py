import random
from insertion import insertion_sort
import os

os.system('clear')

def quicksort(arr, n):
    if n < 2: # base case
        return arr

    else:
        lower_arr = []
        upper_arr = []

        pivot = random.choice(arr)

        for num in arr:
            if num <= pivot:
                lower_arr.append(num)
            else:
                upper_arr.append(num)
        
        arr = quicksort(lower_arr, len(lower_arr)) + \
              quicksort(upper_arr, len(upper_arr))

    return arr

arr = [x for x in range(32)]
random.shuffle(arr)
sorted_arr = quicksort(arr, len(arr))
print(sorted_arr)