######################################################################
# This is a practice file for learning data structures and algorithms. 
# in python.

# This file contains the implementation of the merge sort algorithm.
def merge_sort(array, desc = False):
    
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2

    left_array = merge_sort(array[:mid], desc)
    right_array = merge_sort(array[mid:], desc)

    return merge(left_array, right_array, desc)



def merge(arrayLeft, arrayRight, desc):

    result_array = []
    
    i= j = 0

    if desc:
        while i < len(arrayLeft) and j < len(arrayRight):
            if arrayLeft[i] >= arrayRight[j]:
                result_array.append(arrayLeft[i])
                i += 1
            else:
                result_array.append(arrayRight[j])
                j += 1
    else:
        while i < len(arrayLeft) and j < len(arrayRight):
            if arrayLeft[i] <= arrayRight[j]:
                result_array.append(arrayLeft[i])
                i += 1
            else:
                result_array.append(arrayRight[j])
                j += 1

    result_array += arrayLeft[i:]
    result_array += arrayRight[j:]

    return result_array

