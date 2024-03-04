
def bubbleSortPjN(arr, desc=False):
    """
    Sorts the given array using the bubble sort algorithm.

    Parameters:
    arr (list): The array to be sorted.
    desc (bool, optional): Specifies whether to sort the array in descending order. 
                           Defaults to False, which sorts the array in ascending order.

    Returns:
    list: The sorted array.
    """
    temp = 0
    i = 0

    if desc:
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] < arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
    else:
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

    return arr



array = [67, 16, 8, 12, 15, 6, 3, 9, 5, 55, 10, 98, 25, 87, 33, 41, 17, 99, 63, 88]
print(array)

print(bubbleSortPjN(array))
print(bubbleSortPjN(array, True))

# Test case 5: Array with negative numbers
array5 = [-5, -2, -9, -1, -3]

print("Test case 5: Array with negative numbers")
print("Input array:", array5)
print("Sorted array:", bubbleSortPjN(array5))
print()

array5 = [-5, -2, -9, -1, -3]

print("Test case 5: Array with negative numbers")
print("Input array:", array5)
print("Sorted array:", bubbleSortPjN(array5, True))
print()