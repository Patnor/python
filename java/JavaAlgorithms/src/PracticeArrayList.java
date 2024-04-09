import java.util.Iterator;

public class PracticeArrayList<T> implements Iterable<T> {

    private static final int DEFAULT_CAPACITY = 10;
    private int size;
    private T [] items;

    public PracticeArrayList(){
        doClear();
    }

    public void clear(){
        doClear();
    }
    private void doClear() {
        size = 0;
        ensureCapacity(DEFAULT_CAPACITY);
    }

    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size() == 0;
    }

    public T get(int index){

        if(index < 0 || index >= size())
            throw new ArrayIndexOutOfBoundsException("Index " + index + "; size " + size());

        return items[index];
    }

    public T set(int index, T newItem){

        if(index < 0 || index >= size())
            throw new ArrayIndexOutOfBoundsException("Index " + index + "; size " + size());

        T old = items[index];
        items[index] = newItem;
        return old;
    }

    @SuppressWarnings("unchecked")
    private void ensureCapacity(int newCapacity) {
        if(newCapacity < size())
            return;

        T[] old = items;
        items = (T []) new Object[newCapacity];
        for(int i = 0; i < size(); i++){
            items[i] = old[i];
        }

    }

    @Override
    public Iterator<T> iterator() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'iterator'");
    }
    
}
