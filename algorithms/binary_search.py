array = [0,1,1,3,5,6,11,17]

def binary_search(array, target, left, right):
    mid = int((left+right)/2)
    print(left, right, mid, array[mid], target)
    
    if target == array[mid]:
        return True
    if left > right: 
        return False
    if target < array[mid]:
        return binary_search(array, target, left, mid-1)
    elif target > array[mid]:
        return binary_search(array, target, mid+1, right)
    

print(binary_search(array, 17, 0, len(array) - 1))