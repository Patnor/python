import java.util.Arrays;

public class MergeSortPJN {

    public static int[] merge_sort(int[] array) {

        if (array.length <= 1) {
            return array;
        }

        int mid = array.length / 2;

        int[] a_left = merge_sort(Arrays.copyOfRange(array, 0, mid));
        int[] a_right = merge_sort(Arrays.copyOfRange(array, mid, array.length));

        return merge(a_left, a_right);

    }

    private static int[] merge(int[] left, int[] right) {

        int[] result = new int[left.length + right.length];
        int i = 0;
        int j = 0;

        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                result[i + j] = left[i];
                i++;
            } else {
                result[i + j] = right[j];
                j++;
            }
        }

        while (i < left.length) {
            result[i + j] = left[i];
            i++;
        }

        while (j < right.length) {
            result[i + j] = right[j];
            j++;
        }

        return result;
    }

    public void sayGoodbye() {
        System.out.println("Goodbye!");
    }
}
