######################################################################
# This is a practice file for learning data structures and algorithms. 
# in python.


def merge_sort(array, desc = False):

    if len(array) <= 1:
        return array
    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)



def merge(left, right):

    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def merge_sort_inv (array):

    if len(array) <= 1:
        return array, 0
    
    mid = len(array) // 2
    l_inv = 0
    r_inv = 0

    left, l_inv = merge_sort_inv(array[:mid])
    right, r_inv = merge_sort_inv(array[mid:])

    merged, inv = merge_inv(left, right)

    return merged, l_inv + r_inv + inv

def merge_inv(left, right):
    
    i = j = inv = 0
    result = []

    while i < len(left)  and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv += len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inv
