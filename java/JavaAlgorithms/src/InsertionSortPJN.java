/**
 * The InsertionSortPJN class provides a static method to sort an array 
 * using the Insertion Sort algorithm.
 * 
 * The time complexity of the insertion sort algorithm is O(n^2) in the worst case, 
 * where n is the number of elements in the array. However, it performs well for 
 * small arrays or partially sorted arrays.
 */
public class InsertionSortPJN {
    /**
     * Sorts the given array in ascending order using the Insertion Sort algorithm.
     * 
     * @param arr the array to be sorted
     */
    public static void sort(int [] arr){
        for(int i = 1; i < arr.length; i++){
            int tmp = arr[i];
            int j = i - 1;
             // Enter a while loop if 'j' is greater than 0 and the value 
             // of 'tmp' is less than the value at index 'j' of the array 'arr'             
            while(j >= 0 && tmp < arr[j]){
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = tmp;
        }
    }
}
