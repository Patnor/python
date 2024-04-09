
public class BinaryTreePJN<T extends Comparable<? super T>> {

   /**
 * T: This is a type parameter. It's a placeholder for the actual type that will 
 * be used to create an instance of BinaryTreePJN. When you create an instance 
 * of BinaryTreePJN, you can specify the type, like BinaryTreePJN<Integer> or 
 * BinaryTreePJN<String>.
 *
 * extends Comparable<? super T>: This is a bound on the type parameter T. 
 * It means whatever type T is, it must implement the Comparable interface. 
 * The Comparable interface is used to compare objects, which is often needed in
 *  data structures like binary trees to determine where elements should be inserted.
 *
 * Comparable<? super T>: This is a further restriction on the Comparable interface. 
 * It means the Comparable interface can compare objects of type T or any of its 
 * superclasses. This makes the BinaryTreePJN more flexible because it can now 
 * handle types that are comparable not only to exactly T, but also to any 
 * superclass of T.
 * 
 */

/**
 * This class represents a binary tree data structure.
 *
 * @param <T> the type of element stored in the tree, must implement Comparable
 *            interface
 */


    private BinaryNode<T> root;

    /**
     * Constructs a new binary tree with a null root.
     */
    public BinaryTreePJN() {
        root = null;
    }

    /**
     * Makes the tree empty.
     */
    public void makeEmpty() {
        root = null;
    }

    /**
     * Check if the tree is empty.
     * 
     * @return true if the tree is empty, false otherwise
     */
    public boolean isEmpty() {
        return root == null;
    }

    /**
     * Checks if the tree contains the specified element.
     * Calls a private recursive method to do the actual checking.
     *
     * @param x the element to be checked
     * @return true if the element is found in the tree, false otherwise
     */
    public boolean contains(T x) {
        return contains(x, root);
    }

    /**
     * Finds the minimum element in the binary tree.
     * Calls a private recursive method to do the actual finding.
     * Throws an IllegalStateException if the tree is empty.
     * 
     * @param x the element to be checked
     * @return the minimum element in the tree
     */
    public T findMin(T x) {
        if (isEmpty()) {
            throw new IllegalStateException("Tree is empty");
        }
        return findMin(root).element;
    }

    /**
     * Finds the maximum element in the binary tree.
     * Calls a private non recursive method to do the actual finding.
     * Throws an IllegalStateException if the tree is empty.
     * 
     * @param x the element to be checked
     * @return the maximum element in the tree
     */
    public T findMax(T x) {
        if (isEmpty()) {
            throw new IllegalStateException("Tree is empty");
        }
        return findMax(root).element;
    }

    /**
     * Inserts an element into the binary tree.
     * Calls a private recursive method to do the actual insertion.
     *
     * @param x the element to be inserted
     */
    public void insert(T t) {
        root = insert(t, root);
    }

    /**
     * Removes an element from the binary tree.
     * Calls a private recursive method to do the actual removal.
     *
     * @param x the element to be removed
     */
    public void remove(T x) {
        root = remove(x, root);
    }

    /**
     * Removes an element from the binary tree. This is a recursive method.
     * It starts at the root and then goes to the left or right child depending on
     * the comparison of the element to be removed with the current node's element.
     * If the element is found, it is removed and the tree is updated accordingly.
     *
     * @param x the element to be removed
     * @param t the current node being checked
     * @return the updated node after removal
     */
    private BinaryNode<T> remove(T x, BinaryNode<T> t) {

        // if (t == null) { return t; }: This is the base case of the recursion.
        // If t is null, it means the tree is empty or we've reached a leaf
        // node without finding the value x. In this case, the method returns null.
        if (t == null) {
            return t; // Item not found; do nothing
        }

        int compareResult = x.compareTo(t.element);

        if (compareResult < 0) {
            // If x is less than t.element, the method recursively calls
            // itself to remove x from the left subtree of t.
            t.left = remove(x, t.left);
        } else if (compareResult > 0) {
            // If x is greater than t.element, the method recursively calls
            // itself to remove x from the right subtree of t.
            t.right = remove(x, t.right);
        } else if (t.left != null && t.right != null) { // Two children
            // If x is equal to t.element and t has two children, the method
            // finds the minimum value in the right subtree of t (which is the
            // next in-order successor of t), replaces t.element with that value,
            // and then recursively removes that value from the right subtree.
            t.element = findMin(t.right).element;
            t.right = remove(t.element, t.right);
        } else {
            // If x is equal to t.element and t has one or no child, t is
            // replaced with its non-null child, or null if it has no children.
            t = (t.left != null) ? t.left : t.right;
        }
        return t;
    }

    /**
     * Finds the minimum element in the binary tree. This is a recursive method.
     * It starts at the root and then goes to the left child until it reaches a node
     * that has no left child. That node contains the minimum element.
     *
     * @param t the current node being checked
     * @return the node containing the minimum element, or null if the tree is empty
     */
    private BinaryNode<T> findMin(BinaryNode<T> t) {
        if (t == null) {
            return null;
        } else if (t.left == null) {
            return t;
        } else {
            return findMin(t.left);
        }
    }

    /**
     * Finds the maximum element in the binary tree. This is a non-recursive method.
     * It starts at the root and then goes to the right child until it reaches a
     * node
     * 
     *
     * @param t the current node being checked
     * @return the node containing the maximum element, or null if the tree is empty
     */
    private BinaryNode<T> findMax(BinaryNode<T> t) {
        if (t != null) {
            while (t.right != null) {
                t = t.right;
            }
        }
        return t;
    }

    /**
     * Checks if the tree contains the specified element.
     *
     * @param x the element to be checked
     * @param t the current node being checked
     * @return true if the element is found in the tree, false otherwise
     */
    private boolean contains(T x, BinaryNode<T> t) {
        if (t == null) {
            return false;
        }

        int compareResult = x.compareTo(t.element);

        if (compareResult < 0) {
            return contains(x, t.left);
        } else if (compareResult > 0) {
            return contains(x, t.right);
        } else {
            return true;
        }
    }

    /**
     * Inserts an element into the binary tree.
     *
     * @param x the element to be inserted
     * @param t the current node being checked
     * @return the new node that was inserted
     */
    private BinaryNode<T> insert(T x, BinaryNode<T> t) {
        if (t == null) {
            return new BinaryNode<T>(x, null, null);
        }

        int compareResult = x.compareTo(t.element);

        if (compareResult < 0) {
            return insert(x, t.left);
        } else if (compareResult > 0) {
            return insert(x, t.right);
        } else {
            ; // Duplicate; do nothing
        }

        return t;
    }

    /**
     * This inner class represents a node in the binary tree.
     *
     * @param <T> the type of element stored in the node, must implement Comparable
     *            interface
     */
    private static class BinaryNode<T> {
        T element;
        BinaryNode<T> left;
        BinaryNode<T> right;

        /**
         * Constructs a new BinaryNode with the specified element.
         *
         * @param theElement the element to be stored in the node
         */
        private BinaryNode(T theElement) {
            this(theElement, null, null);
        }

        /**
         * Constructs a new BinaryNode with the specified element, left child, and right
         * child.
         *
         * @param theElement the element to be stored in the node
         * @param lt         the left child of the node
         * @param rt         the right child of the node
         */
        private BinaryNode(T theElement, BinaryNode<T> lt, BinaryNode<T> rt) {
            element = theElement;
            left = lt;
            right = rt;
        }
    }

}
