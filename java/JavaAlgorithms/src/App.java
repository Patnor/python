import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");



        // StackPJN
        System.out.println("StackPJN");
        StackPJN<Integer> stack = new StackPJN<>(); 
        stack.push(1);
        stack.push(2);
        stack.push(3);

        System.out.println("popping the top element: " + stack.pop());
        System.out.println("popping the top element: " + stack.pop());
        System.out.println("popping the top element: " + stack.pop());
        System.out.println();
   
        // LinkedListDoublePJN
         // LinkedListDoublePJN
         LinkedListDoublePJN<Integer> linkedList = new LinkedListDoublePJN<>();
         linkedList.add(1);
         linkedList.add(2);
         linkedList.add(3);
         linkedList.add(4);
         linkedList.add(5);
         linkedList.remove(3);

         System.out.println("retrieving the first element: " + linkedList.get(0));

        System.out.println("printing the Double linked list....");
        for(int i = 0; i < linkedList.size(); i++){
            System.out.println(linkedList.get(i));
        }

        

        // MyArrayList
        MyArrayList<Integer> list = new MyArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.remove(3);
        

        System.out.println("printing the list....");
        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }

        // merge sort
        int [] myArray = {1,6,2,5,4};
        System.out.println(Arrays.toString(MergeSortPJN.merge_sort(myArray)));

        int[] array4 = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
        System.out.println(Arrays.toString(MergeSortPJN.merge_sort(array4)));

        // Test case 5: Array with negative numbers
        int[] array5 = {-5, -2, 6, -9, -1, -3};
        System.out.println(Arrays.toString(MergeSortPJN.merge_sort(array5)));


        // insertion sort
        int [] myArray2 = {1,6,2,5,4, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
        int[] arrayInsert5 = {-5, -2, 6, -9, -1, -3};
        InsertionSortPJN.sort(myArray2);
        InsertionSortPJN.sort(arrayInsert5);
        System.out.println(Arrays.toString(myArray2));
        System.out.println(Arrays.toString(arrayInsert5));

        // string manipulations
        StringManipulation.printMissingNumber(new int[] {1, 2, 3, 4, 6, 7, 9, 8}, 10);
        // Only one missing number in array
        int[] iArray = new int[]{1, 2, 3, 5};
        int missing = StringManipulation.getMissingNumber(iArray, 5);
        System.out.printf("Missing number in array %s is %d %n", 
                            Arrays.toString(iArray), missing);

        
        // Create an array of 1 - 100 with 1 element missing
        int[] array = new int[99];
        int missingNumber = 42; // Choose any number between 1 and 100 as the missing number

        int index = 0;
        for (int i = 1; i <= 100; i++) {
            if (i == missingNumber) {
                continue; // Skip the missing number
            }
            array[index] = i;
            index++;
        }

        System.out.println(Arrays.toString(array));
        System.out.println(StringManipulation.getMissingNumberSumOfSeries(array));

        // test practice file
        int[] arrayIn = {67, 16, 8, 12, 15, 6, 3, 9, 5, 55, 10, 98, 25, 87, 33, 41, 17, 99, 63, 88};
        InsertionSortPJN.sort(arrayIn);
        System.out.println(Arrays.toString(arrayIn ));
        
       // bubble sort
       int[] arrayBub = {67, 16, 8, 12, 15, 6, 3, 9, 5, 55, 10, 98, 25, 87, 33, 41, 17, 99, 63, 88};
         BubbleSortPJN.bubbleSortPJN(arrayBub);
         System.out.println(Arrays.toString(arrayBub));
    }
}
