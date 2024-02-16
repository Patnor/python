

def MergeSortInv(array):
 
    if len(array) <= 1:
        return array, 0
    
    mid = len(array) // 2
    invL = 0
    invR = 0

    left, invL = MergeSortInv(array[:mid])
    right, invR = MergeSortInv(array[mid:])

    merged, inv = mergeInv(left, right)

    return merged, invL + invR + inv

def mergeInv(left, right):
    result = []
    i = j = inv = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv += len(left) - i
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result, inv
