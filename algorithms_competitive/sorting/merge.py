import random

def merge_sort(arr, n):
    # base case
    if n < 2:
        return arr
    median = int(n / 2)
    left_arr  = arr[:median]
    right_arr = arr[median:]

    arr = merge_sort(left_arr, len(left_arr)) + merge_sort(right_arr, len(right_arr))

arr = [x for x in range(32)]
random.shuffle(arr)
sorted_arr = merge_sort(arr, len(arr))
print(sorted_arr)