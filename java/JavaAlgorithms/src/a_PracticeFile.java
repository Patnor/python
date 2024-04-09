public class a_PracticeFile {
    

public class BinaryTree<T extends Comparable<? super T>>{

    private BinaryNode<T> root;

    public BinaryTree(){
        root = null;
    }

    public boolean isEmpty(){
        return root == null;
    }

    public void makeEmpty(){
        root = null;
    }

    public  T findMin(){
        if(isEmpty())
            throw new IllegalStateException();
        return findMin(root).data;
    }
    private BinaryNode<T> findMin(BinaryNode<T> node){

        if(node != null)
            while(node.lNode != null)
                node = node.lNode;
            

        return  node;
    }

    public T findMax(){
        if(isEmpty())
            throw new IllegalStateException();
        return findMax(root).data;
    }

    private BinaryNode<T> findMax(BinaryNode<T> node){

        if(node == null)
            return null;
        else if( node.rNode == null)
            return node;
        
        return findMax(node.rNode);
    }


    


    public boolean contains(T value){
        return contains(value, root);
    }

    private boolean contains( T value, BinaryNode<T> node){

        if(node == null)
            return false;

        int compareResult = value.compareTo(node.data);

        if(compareResult < 0)
            return contains(value, node.lNode);
        if(compareResult > 0)
            return contains(value, node.rNode);
        else
            return true;
    }


    private static class BinaryNode<T>{
        T data;
        BinaryNode<T> lNode;
        BinaryNode<T> rNode;

        BinaryNode( T item){
            // calls the BinaryNode ( T item, BinaryNode<T> left, BinaryNode<T> right) constructor 
            this(item, null, null);
        }

        BinaryNode ( T item, BinaryNode<T> left, BinaryNode<T> right){
            data = item;
            lNode = left;
            rNode = right;
            }
        }
    }


}