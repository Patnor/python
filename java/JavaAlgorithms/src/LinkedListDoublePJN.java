import java.util.Iterator;

/**
 * LinkedListDoublePJN is a generic doubly linked list implementation in Java.
 * It allows adding, removing, and modifying elements at specific positions in
 * the list.
 * The list can be iterated using an iterator.
 *
 * @param <T> the type of elements stored in the list
 */
/**
 * This class represents a doubly linked list implementation in Java.
 * It provides methods to add, remove, get, and set elements in the list.
 * It also implements the Iterable interface to support iteration over the elements in the list.
 *
 * @param <T> the type of elements stored in the list
 */
/**
 * Represents a doubly linked list implementation in Java.
 *
 * @param <T> the type of elements stored in the list
 */
public class LinkedListDoublePJN<T> implements Iterable<T> {

    private int theSize;
    private int modCount = 0;
    private Node<T> beginMarker;
    private Node<T> endMarker;

    /**
     * Constructs an empty LinkedListDoublePJN.
     */
    public LinkedListDoublePJN() {
        doClear();
    }

    /**
     * Removes all elements from the list.
     */
    public void clear() {
        doClear();
    }

    /**
     * Returns the number of elements in the list.
     *
     * @return the number of elements in the list
     */
    public int size() {
        return theSize;
    }

    /**
     * Checks if the list is empty.
     *
     * @return true if the list is empty, false otherwise
     */
    public boolean isEmpty() {
        return size() == 0;
    }

    /**
     * Adds an element to the end of the list.
     *
     * @param data the element to be added
     * @return true (as specified by the Collection interface)
     */
    public boolean add(T data) {
        add(size(), data);
        return true;
    }

    /**
     * Inserts an element at the specified index in the list.
     *
     * @param index the index at which the element should be inserted
     * @param data  the element to be inserted
     */
    public void add(int index, T data) {
        addBefore(getNode(index, 0, size()), data);
    }

    /**
     * Returns the element at the specified index in the list.
     *
     * @param index the index of the element to be retrieved
     * @return the element at the specified index
     */
    public T get(int index) {
        return getNode(index).data;
    }

    /**
     * Replaces the element at the specified index in the list with the specified element.
     *
     * @param index  the index of the element to be replaced
     * @param newVal the new value to be set
     * @return the old value at the specified index
     */
    public T set(int index, T newVal) {
        Node<T> p = getNode(index);
        T oldVal = p.data;
        p.data = newVal;
        return oldVal;
    }

    /**
     * Removes the element at the specified index from the list.
     *
     * @param index the index of the element to be removed
     * @return the removed element
     */
    public T remove(int index) {
        return remove(getNode(index));
    }

    /**
     * Returns an iterator over the elements in the list.
     *
     * @return an iterator over the elements in the list
     */
    @Override
    public Iterator<T> iterator() {
        return new LinkedListDoublePJNIterator();
    }

    // ==========================================================================
    // private methods

    /**
     * Clears the list by resetting the markers and size.
     */
    private void doClear() {
        beginMarker = new Node<T>(null, null, null);
        endMarker = new Node<T>(null, beginMarker, null);
        beginMarker.next = endMarker;

        theSize = 0;
        modCount++;
    }

    /**
     * Adds a new node with the specified data before the given node.
     *
     * @param node the node before which the new node should be added
     * @param x    the data of the new node
     */
    private void addBefore(Node<T> node, T x) {
        // create new node with data x, and set its previous and next node
        Node<T> newNode = new Node<>(x, node.pre, node);
        // set the previous node's next to the new node
        newNode.pre.next = newNode;
        // set the next node's previous to the new node
        node.pre = newNode;
        theSize++;
        modCount++;
    }

    /**
     * Removes the specified node from the list.
     *
     * @param p the node to be removed
     * @return the data of the removed node
     */
    private T remove(Node<T> p) {
        // set the next node's previous to the previous node
        p.next.pre = p.pre;
        // set the previous node's next to the next node
        p.pre.next = p.next;
        theSize--;
        modCount++;

        return p.data;
    }

    /**
     * Returns the node at the specified index in the list.
     *
     * @param index the index of the node to be retrieved
     * @return the node at the specified index
     */
    private Node<T> getNode(int index) {
        return getNode(index, 0, size() - 1);
    }

    /**
     * Returns the node at the specified index in the list within the given range.
     *
     * @param index the index of the node to be retrieved
     * @param lower the lower bound of the range
     * @param upper the upper bound of the range
     * @return the node at the specified index
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    private Node<T> getNode(int index, int lower, int upper) {
        Node<T> p;

        if (index < lower || index > upper) {
            throw new IndexOutOfBoundsException();
        }

        // if index is less than half of the size, start from the beginning
        if (index < size() / 2) {
            p = beginMarker.next;
            for (int i = 0; i < index; i++) {
                p = p.next;
            }
        } else { // if index is greater than half of the size, start from the end
            p = endMarker;
            for (int i = size(); i > index; i--) {
                p = p.pre;
            }
        }

        return p;
    }

    // ==========================================================================
    // private inner class

    /**
     * Represents a node in the doubly linked list.
     *
     * @param <T> the type of data stored in the node
     */
    private static class Node<T> {
        public T data;
        public Node<T> pre;
        public Node<T> next;

        /**
         * Constructs a new node with the specified data, previous node, and next node.
         *
         * @param data the data to be stored in the node
         * @param pre  the previous node
         * @param next the next node
         */
        public Node(T data, Node<T> pre, Node<T> next) {
            this.data = data;
            this.pre = pre;
            this.next = next;
        }
    }

    /**
     * Represents an iterator over the elements in the doubly linked list.
     */
    private class LinkedListDoublePJNIterator implements Iterator<T> {

        private Node<T> current = beginMarker.next;
        private int expectedModCount = modCount;
        private boolean okToRemove = false;

        @Override
        public boolean hasNext() {
            return current != endMarker;
        }

        @Override
        public T next() {
            if (modCount != expectedModCount)
                throw new java.util.ConcurrentModificationException();
            if (!hasNext())
                throw new java.util.NoSuchElementException();

            // get the data of the current node, and move to the next node
            T nextItem = current.data;
            current = current.next;
            // set okToRemove to true
            okToRemove = true;
            return nextItem;
        }

        /**
         * Removes the last element returned by the iterator from the underlying collection.
         *
         * @throws java.util.ConcurrentModificationException if the list was modified outside of the iterator
         * @throws IllegalStateException                     if the {@code next} method has not yet been called,
         *                                                   or the {@code remove} method has already been called
         */
        public void remove() {
            if (modCount != expectedModCount)
                throw new java.util.ConcurrentModificationException();
            if (!okToRemove)
                throw new IllegalStateException();

            // remove the previous node of the current node
            // (since the current node is already moved to the next node)
            LinkedListDoublePJN.this.remove(current.pre);
            expectedModCount++;
            okToRemove = false;
        }
    }
}
