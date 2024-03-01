# Quicksort is a divide and conquer algorithm. It first divides a large list 
# into two smaller sub-lists and then recursively sort the sub-lists.
# best case: pivot is median. median is middle element of a sorted array
# worst case: pivot is first or last element of a sorted array.
# To avoid worst case, we can choose pivot as median of first, middle and last 
# element of array.

from numpy import Infinity
import random

def choose_pivot(array, selection):
    if selection == 1:
        pivot = random.choice(array)
    elif selection == 2:
        print([array[0], array[len(array)//2], array[-1]])
        pivot = sorted([array[0], array[len(array)//2], array[-1]])[1]
        print(array)
    else:
        raise ValueError("Invalid selection parameter")
    
    return pivot

array = [67, 16, 8, 12, 15, 6, 3, 9, 5,55,10,98,25,87,33,41,17,99, 63,88]



def quicksortPJN(array):
    if len(array) <= 1:
        return array
    
    pivot = choose_pivot(array, 2)
    print(pivot)

    print(array)


def hoare_partition(array, low, high):
    pivot = array[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


def lomuto_partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

quicksortPJN(array, 0, len(array) - 1)
quicksortPJN(array)

