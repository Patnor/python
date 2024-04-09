package test;

import static org.junit.Assert.assertArrayEquals;

import org.junit.jupiter.api.*;

import main.InsertionSortPJN;



public class InsertionSortPJNTest {

    @Test
    public void testSort_emptyArray() {
        int[] arr = new int[0];
        InsertionSortPJN.sort(arr);
        assertArrayEquals(new int[0], arr);
    }

    @Test
    public void testSort_singleElementArray() {
        int[] arr = new int[]{5};
        InsertionSortPJN.sort(arr);
        assertArrayEquals(new int[]{5}, arr);
    }

    @Test
    public void testSort_multipleElementsArray() {
        int[] arr = new int[]{5, 3, 8, 1, 9, 2};
        InsertionSortPJN.sort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 5, 8, 9}, arr);
    }

    @Test
    public void testSort_alreadySortedArray() {
        int[] arr = new int[]{1, 2, 3, 4, 5};
        InsertionSortPJN.sort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, arr);
    }

    @Test
    public void testSort_reverseSortedArray() {
        int[] arr = new int[]{5, 4, 3, 2, 1};
        InsertionSortPJN.sort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, arr);
    }
}