import java.util.Iterator;

/**
 * The MyArrayList class represents a generic dynamic array implementation.
 * It provides methods to add, remove, get, set, and iterate over elements in the array.
 * @param <T> the type of elements in the array
 */
public class MyArrayList<T> implements Iterable<T>{

    private static final int DEFAULT_CAPACITY = 10;

    private int theSize;
    private T[] theItems;

    /**
     * Constructs an empty MyArrayList with the default initial capacity.
     */
    public MyArrayList(){
        doClear();
    }

    /**
     * Removes all elements from the MyArrayList.
     */
    public void clear(){
        doClear();
    }

    private void doClear() {
        theSize = 0;
        ensureCapacity(DEFAULT_CAPACITY);
    }

    /**
     * Returns the number of elements in the MyArrayList.
     * @return the number of elements in the MyArrayList
     */
    public int size(){
        return theSize;
    }

    /**
     * Checks if the MyArrayList is empty.
     * @return true if the MyArrayList is empty, false otherwise
     */
    public boolean isEmpty(){
        return size() == 0;
    }

    /**
     * Trims the capacity of the MyArrayList to the current size.
     */
    public void trimToSize(){
        ensureCapacity(size());
    }
     
    /**
     * Returns the element at the specified index in the MyArrayList.
     * @param index the index of the element to retrieve
     * @return the element at the specified index
     * @throws ArrayIndexOutOfBoundsException if the index is out of range
     */
    public T get(int index){
        if(index < 0 || index >= size()){
            throw new ArrayIndexOutOfBoundsException();
        }
        return theItems[index];
    }

    /**
     * Replaces the element at the specified index in the MyArrayList with the specified element.
     * @param index the index of the element to replace
     * @param newVal the new value to set at the specified index
     * @return the old value at the specified index
     * @throws ArrayIndexOutOfBoundsException if the index is out of range
     */
    public T set(int index, T newVal){
        if(index < 0 || index >= size()){
            throw new ArrayIndexOutOfBoundsException();
        }
        T old = theItems[index];
        theItems[index] = newVal;
        return old;
    }

    /**
     * Ensures that the MyArrayList has the specified capacity.
     * @param newCapacity the new capacity to set for the MyArrayList
     */
    private void ensureCapacity(int newCapacity) {
        if(newCapacity < theSize)
            return;
        
        T[] old = theItems;
        // casting an object array to a generic array
        theItems = (T[]) new Object[newCapacity];

        for(int i = 0; i < size(); i++){
            theItems[i] = old[i];
        }
    }

    /**
     * Adds the specified element to the end of the MyArrayList.
     * @param x the element to add
     * @return true
     */
    public boolean add(T x){
        add(size(), x);
        return true;
    }

    private void add(int index, T x) {
        if(theItems.length == size()){
            ensureCapacity(size() * 2 + 1);
        }
        for(int i = theSize; i > index; i--){
            theItems[i] = theItems[i - 1];
        }
        theItems[index] = x;

        theSize++;
    }

    /**
     * Removes the element at the specified index in the MyArrayList.
     * @param index the index of the element to remove
     * @return the removed element
     */
    public T remove(int index){
        T removedItem = theItems[index];
        for(int i = index; i < size() - 1; i++){
            theItems[i] = theItems[i + 1];
        }
        theSize--;
        return removedItem;
    }

    @Override
    public Iterator<T> iterator() {
        return new ArrayListIterator();
    }

    // inner class
    private class ArrayListIterator implements Iterator<T>{

        private int current = 0;

        @Override
        public boolean hasNext() {
            return current < size();
        }

        @Override
        public T next() {
            if(!hasNext()){
                throw new java.util.NoSuchElementException();
            }
            return theItems[current++];
        }

        @Override
        public void remove() {
            MyArrayList.this.remove(--current);
        }
    }
}
