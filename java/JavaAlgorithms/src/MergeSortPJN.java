import java.util.Arrays;

/**
 * The MergeSortPJN class provides a static method for performing merge sort on an array of integers.
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
