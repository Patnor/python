"""
This file contains the implementation of the merge sort algorithm.

Time Complexity:
The time complexity of merge sort is O(n log n), 
where n is the number of elements in the array.
"""

# Function to perform merge sort on an array
def merge_sort(array,  desc = False):
    """
    Sorts an array using the merge sort algorithm.

    Parameters:
    array (list): The array to be sorted.
    desc (bool): A flag to indicate whether to sort the array in 
                descending order. Defaults to False.

    Returns:
    list: The sorted array.
    """

    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid], desc)  # Recursively sort the left half of the array
    right = merge_sort(array[mid:], desc)  # Recursively sort the right half of the array

    # Merge the sorted left and right halves
    return merge(left, right, desc)

# Function to merge two sorted arrays
def merge(left, right, desc):
    """
    Merges two sorted arrays into a single sorted array.

    Parameters:
    left (list): The left sorted array.
    right (list): The right sorted array.
    desc (bool): A flag to indicate whether to merge the arrays in 
                descending order. Defaults to False.

    Returns:
    list: The merged sorted array.
    """

    result = []  # Initialize an empty list to store the merged result
    i = j = 0  # Initialize pointers for the left and right arrays

    # Compare elements from the left and right arrays and add the smaller element to the result
    if desc:
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    else:
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    # Add any remaining elements from the left or right array to the result
    result += left[i:]
    result += right[j:]

    return result

