import java.util.Arrays;

/**
 * The MergeSortPJN class provides a static method for performing merge sort 
 * on an array of integers.
 * 
 * 
 * The time complexity of the merge sort algorithm is O(n log n), where 'n' 
 * represents the number of elements in the input array.
 * 
 *  Merge sort is a divide-and-conquer algorithm that works by recursively 
 * dividing the input array into smaller subarrays, sorting them, and then 
 * merging them back together. Here's a step-by-step breakdown of the merge 
 * sort algorithm:
 * 
 *  Divide: The input array is divided into two halves repeatedly until each 
 * subarray contains only one element. This process takes O(log n) time because 
 * the array is divided in half at each level of recursion.
 * 
 *  Merge: The sorted subarrays are then merged back together in a sorted 
 * manner. The merging process compares the elements from both subarrays and 
 * places them in the correct order. This merging step takes O(n) time because 
 * each element in the input array is visited once during the merging process.
 * 
 * Repeat: Steps 1 and 2 are repeated recursively until the entire array is sorted.
 * 
 * Since the divide step takes O(log n) time and the merge step takes O(n) time, 
 * the overall time complexity of merge sort is O(n log n). This time complexity 
 * remains the same regardless of the initial order of the elements in the input 
 * array.
 * 
 * Merge sort is known for its efficiency and stability, making it a popular 
 * choice for sorting large datasets. However, it does require additional space 
 * for the temporary arrays used during the merging process, which results in a 
 * space complexity of O(n). 
 */
public class MergeSortPJN {

    /**
     * Sorts the given array using merge sort algorithm.
     *
     * @param array the array to be sorted
     * @return the sorted array
     */
    public static int[] merge_sort(int[] array) {

        if (array.length <= 1) {
            return array;
        }

        int mid = array.length / 2;

        int[] a_left = merge_sort(Arrays.copyOfRange(array, 0, mid));
        int[] a_right = merge_sort(Arrays.copyOfRange(array, mid, array.length));

        return merge(a_left, a_right);
    }

    /**
     * Merges two sorted arrays into a single sorted array.
     *
     * @param left the left array
     * @param right the right array
     * @return the merged sorted array
     */
    private static int[] merge(int[] left, int[] right) {

        int[] result = new int[left.length + right.length];
        int i = 0;
        int j = 0;

        // Merge the left and right arrays into a single sorted array
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                result[i + j] = left[i];
                i++;
            } else {
                result[i + j] = right[j];
                j++;
            }
        }
        
        // Copy remaining elements from left array
        while (i < left.length) {
            result[i + j] = left[i];
            i++;
        }

        // Copy remaining elements from right array
        while (j < right.length) {
            result[i + j] = right[j];
            j++;
        }

        return result;
    }
}
