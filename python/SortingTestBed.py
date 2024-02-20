import MergeSortPJN as ms
import random
import MergeSortInv as msi
import MatrixMultStandard as mms
import MatrixMultStrassen as mmSt


# array = [random.randint(0, 3000) for _ in range(208)]

# print(array)

# sorted_array = ms.merge_sort(array)

# print()
# print("Sorted array: ")
# print(sorted_array)

# Test script for MergeSortPJN.py

# arrayInv = [6,5,4,3,2,1]

# sorted_arrayInv, inversions = msi.MergeSortInv(arrayInv)
# print()
# print("Sorted array: ", sorted_arrayInv)
# print("Inversions: ", inversions)


# *****************************************************************
#                    Matrix Multiplication Standard

matrixA = [[1, 2], [4, 5]]
matrixB = [[5, 6], [7, 8]]

matrixZ = mms.matrixMultStandard(matrixA, matrixB)

# expected output: [[19, 22], [55, 64]]
print(matrixZ)