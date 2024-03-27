public class StackPJN<T> {
    LinkedListDoublePJN<T> stack = new LinkedListDoublePJN<T>();

    public void push(T value){
        stack.add(value);
    }

    public T pop(){
        return stack.remove(stack.size() - 1);
    }

}
