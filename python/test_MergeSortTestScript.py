import random
import time
import MergeSortPJN as ms
import PracticeFile as pf



# Test case 2: Large sorted array
array2 = [i for i in range(1000000)]
start_time2 = time.time()
sorted_array2 = ms.merge_sort(array2)
end_time2 = time.time()
print("Test case 2: Large sorted array")
print("Input array size:", len(array2))
print("Sorted array size:", len(sorted_array2))
print("Execution time:", end_time2 - start_time2, "seconds")
print()

# Test case 3: Large reverse sorted array
array3 = [i for i in range(1000000, 0, -1)]
start_time3 = time.time()
sorted_array3 = ms.merge_sort(array3)
end_time3 = time.time()
print("Test case 3: Large reverse sorted array")
print("Input array size:", len(array3))
print("Sorted array size:", len(sorted_array3))
print("Execution time:", end_time3 - start_time3, "seconds")
print()

# Test case 1: Large random array
array1 = [random.randint(1, 100000) for _ in range(1000000)]
start_time1 = time.time()
sorted_array1 = ms.merge_sort(array1)
end_time1 = time.time()
print("Test case 1: Large random array")
print("Input array size:", len(array1))
print("Sorted array size:", len(sorted_array1))
print("Execution time:", end_time1 - start_time1, "seconds")
print()