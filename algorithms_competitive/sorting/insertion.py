import random

def insertion_sort(arr, n):
    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[i - j - 1]:
                arr.insert(i - j, arr.pop(i))
                break
        else:
            arr.insert(0, arr.pop(i))
    return arr

if __name__ == "__main__":
    n = 50
    arr = [random.randrange(n) for _ in range(n)]
    print(list(dict.fromkeys(arr)), len(list(dict.fromkeys(arr))))
    sorted_arr = insertion_sort(arr, len(arr))
    print(sorted_arr)