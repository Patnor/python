import MergeSortPJN as ms
import random
import MergeSortInv as msi


# array = [random.randint(0, 3000) for _ in range(208)]

# print(array)

# sorted_array = ms.merge_sort(array)

# print()
# print("Sorted array: ")
# print(sorted_array)

# Test script for MergeSortPJN.py

arrayInv = [6,5,4,3,2,1]

sorted_arrayInv, inversions = msi.MergeSortInv(arrayInv)
print()
print("Sorted array: ", sorted_arrayInv)
print("Inversions: ", inversions)