import python.MergeSortPJN as ms
import random


array = [random.randint(0, 3000) for _ in range(208)]

print(array)

sorted_array = ms.merge_sort(array)

print()
print("Sorted array: ")
print(sorted_array)

# Test script for MergeSortPJN.py

