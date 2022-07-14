def merge(left_arr, right_arr, left_n, right_n):
    merge_arr = []
    left_i = 0
    right_i = 0
    while left_i < left_n or right_i < right_n:
        if left_i < left_n and left_arr[left_i] < right_arr[right_i]:
            merge_arr.append(left_arr[left_i])
            left_i += 1
        elif right_i < right_n:
            merge_arr.append(right_arr[right_i])
            right_i += 1
    return merge_arr

a = [5,6,12]
b = [1,9,10]
# a = [1,2,3]
# b = [4,5,6]
merge_arr = merge(a,b, len(a), len(b))
print(merge_arr)