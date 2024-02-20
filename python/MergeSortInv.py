
"""
    The time complexity of the MergeSortInv function is O(n log n), 
    where n is the size of the input array
"""

def MergeSortInv(array):
    """
    Sorts an array using the merge sort algorithm and counts the number of 
    inversions.

    Args:
        array (list): The array to be sorted.

    Returns:
        tuple: A tuple containing the sorted array and the number of inversions.

    Example:
        >>> MergeSortInv([4, 2, 1, 3])
        ([1, 2, 3, 4], 3)
    """
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
    """
    Merge two sorted lists and count the number of inversions.

    Args:
        left (list): The left sorted list.
        right (list): The right sorted list.

    Returns:
        tuple: A tuple containing the merged sorted list and the number of 
        inversions.

    Example:
        >>> mergeInv([1, 3, 5], [2, 4, 6])
        ([1, 2, 3, 4, 5, 6], 0)
    """
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
