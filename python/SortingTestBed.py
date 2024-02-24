import MergeSortPJN as ms
import random
import MergeSortInv as msi
import MatrixMultStandard as mms
import MatrixMultStrassen as mmSt
import PracticeFile as pf

# *****************************************************************
#               merge sort
array = [random.randint(0, 3000) for _ in range(208)]

print(array)

sorted_array = ms.merge_sort(array, True)

print()
print("Sorted array: ")
print(sorted_array)



# *****************************************************************
#               merge sort with inversions
arrayInv = [6,5,4,3,2,1]

sorted_arrayInv, inversions = pf.merge_sort_inv(arrayInv)
print()
print("Sorted array: ", sorted_arrayInv)
print("Inversions: ", inversions)


# *****************************************************************
#                    Matrix Multiplication Standard

matrixA = [[1, 2], [4, 5]]
matrixB = [[5, 6], [7, 8]]
matrixC = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrixD = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]

matrixZ = mms.matrixMultStandard(matrixA, matrixB)
matrixCD = mms.matrixMultStandard(matrixC, matrixD)

# expected output: [[19, 22], [55, 64]]
# expected output: [[250, 260, 270, 280], [618, 644, 670, 696], 
#                   [986, 1028, 1070, 1112], [1354, 1412, 1470, 1528]]
print(matrixZ)
print(matrixCD)