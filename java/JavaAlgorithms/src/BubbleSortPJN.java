public class BubbleSortPJN {
    /**
     * Sorts an array of integers using the Bubble Sort algorithm.
     *
     * @param array the array of integers to be sorted
     * @return the sorted array
     */
    public static int[] bubbleSortPJN(int[] array) {

        int temp;
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length - 1; j++) {
                if (array[j] > array[j + 1]) {
                    temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        return array;
    }
}
