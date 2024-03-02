import java.util.Arrays;
import java.util.BitSet;

public class StringManipulation {
    public static void printMissingNumber(int[] nums, int count) {
        int missingCount = count - nums.length;
        BitSet bitSet = new BitSet(count);
        for (int num : nums) {
            bitSet.set(num - 1);
        }
        System.out.printf("Missing numbers in integer array %s, with total number %d is %n", Arrays.toString(nums), count);
        int lastMissingIndex = 0;
        for (int i = 0; i < missingCount; i++) {
            lastMissingIndex = bitSet.nextClearBit(lastMissingIndex);
            System.out.println(++lastMissingIndex);
        }
    }


    public static int getMissingNumber(int[] numbers, int totalCount) {
        int expectedSum = totalCount * ((totalCount + 1) / 2);
        int actualSum = 0;
        for (int i : numbers) {
            actualSum += i;
        }
 
        return expectedSum - actualSum;
    }

    // Sum of the series Formula: n (n+1)/2 (but only work for one missing number)
    public static int getMissingNumberSumOfSeries(int [] numbers) {
        int n  = numbers.length + 1;
        int sum = n * (n + 1) / 2;
        int actualSum = 0;
        for (int i : numbers) {
            actualSum += i;
        }
        System.out.println("Sum of the series: " + sum);
        System.out.println("Sum of the numbers: " + actualSum);
        return sum - actualSum;
    }
}
