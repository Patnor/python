import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
   
        // Rest of your code...
        int [] myArray = {1,6,2,5,4};
        System.out.println(Arrays.toString(MergeSortPJN.merge_sort(myArray)));

        int[] array4 = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
        System.out.println(Arrays.toString(MergeSortPJN.merge_sort(array4)));

        // Test case 5: Array with negative numbers
        int[] array5 = {-5, -2, 6, -9, -1, -3};
        System.out.println(Arrays.toString(MergeSortPJN.merge_sort(array5)));


       
    }
}
