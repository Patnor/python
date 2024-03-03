# insertion sort

def insertionsSort(arr):
  
    for i in range( 1, len(arr) ):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


array = [67, 16, 8, 12, 15, 6, 3, 9, 5, 55, 10, 98, 25, 87, 33, 41, 17, 99, 63, 88]
print(array)
insertionsSort(array)
print(array)

