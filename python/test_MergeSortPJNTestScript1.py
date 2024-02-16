import MergeSortPJN as ms
import PracticeFile as pf
import random
import time

# Test case 1: Empty array
array1 = []
sorted_array1 = ms.merge_sort(array1, True)
print("Test case 1: Empty array")
print("Input array:", array1)
print("Sorted array:", sorted_array1)
print()

# Test case 2: Array with one element
array2 = [5]
sorted_array2 = ms.merge_sort(array2, True)
print("Test case 2: Array with one element")
print("Input array:", array2)
print("Sorted array:", sorted_array2)
print()

# Test case 3: Array with two elements
array3 = [9, 2]
array3 = ms.merge_sort(array3, True)
print("Test case 3: Array with two elements")
print("Input array:", array3)
print("Sorted array:", 3)
print()

# Test case 4: Array with duplicate elements
array4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_array4 = ms.merge_sort(array4, True)
print("Test case 4: Array with duplicate elements")
print("Input array:", array4)
print("Sorted array:", sorted_array4)
print()

# Test case 5: Array with negative numbers
array5 = [-5, -2, -9, -1, -3]
sorted_array5 = ms.merge_sort(array5, True)
print("Test case 5: Array with negative numbers")
print("Input array:", array5)
print("Sorted array:", sorted_array5)
print()

# Test case 6: Array with already sorted elements
array6 = [1, 2, 3, 4, 5]
sorted_array6 = ms.merge_sort(array6, True)
print("Test case 6: Array with already sorted elements")
print("Input array:", array6)
print("Sorted array:", sorted_array6)
print()

# Test case 7: Array with reverse sorted elements
array7 = [5, 4, 3, 2, 1]
sorted_array7 = ms.merge_sort(array7, True)
print("Test case 7: Array with reverse sorted elements")
print("Input array:", array7)
print("Sorted array:", sorted_array7)
print()

# Test case 2: Large sorted array
array8 = [i for i in range(1000000)]
start_time2 = time.time()
sorted_array8 = ms.merge_sort(array8)
end_time2 = time.time()
print("Test case 2: Large sorted array")
print("Input array size:", len(array8))
print("Sorted array size:", len(sorted_array8))
print("Execution time:", end_time2 - start_time2, "seconds")
print()

# Test case 3: Large reverse sorted array
array9 = [i for i in range(1000000, 0, -1)]
start_time3 = time.time()
sorted_array9 = ms.merge_sort(array9)
end_time3 = time.time()
print("Test case 3: Large reverse sorted array")
print("Input array size:", len(array9))
print("Sorted array size:", len(sorted_array9))
print("Execution time:", end_time3 - start_time3, "seconds")
print()

# Test case 1: Large random array
array10 = [random.randint(1, 100000) for _ in range(1000000)]
start_time1 = time.time()
sorted_array10 = ms.merge_sort(array10)
end_time1 = time.time()
print("Test case 1: Large random array")
print("Input array size:", len(array10))
print("Sorted array size:", len(sorted_array10))
print("Execution time:", end_time1 - start_time1, "seconds")
print()
