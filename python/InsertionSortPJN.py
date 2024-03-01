

"""
The time complexity of the insertion sort algorithm is O(n^2) in the worst case, 
where n is the number of elements in the array. However, it performs well for 
small arrays or partially sorted arrays.
"""


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def insertion2(arr):
    # Traverse through 1 to len(arr)
    # start at  i = 1
    for i in range(1, len(arr)):
        
        tmp = arr[i]
        j = i-1
        # if temp is less then move the element arr[j] to arr[j+1]. Keep doing 
        # this until we find the correct position for temp
        while j >= 0 and tmp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        # because we decremented j, we need to increment it back to the correct
        
        arr[j+1] = tmp


array = [67, 16, 8, 12, 15, 6, 3, 9, 5, 55, 10, 98, 25, 87, 33, 41, 17, 99, 63, 88]
print(array)
insertion2(array)
print(array)
# insertionSort(array)

# print(array)
