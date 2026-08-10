class MinStack {

    Stack<Integer> stack;
    Stack<Integer> min;

    public MinStack() {
        stack = new Stack<>();
        min = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(new Integer(val));
        if (min.isEmpty()){
            min.push(new Integer(val));
        }
        else{
            min.push(new Integer(Math.min(val, min.peek())));
        }
    }
    
    public void pop() {
        stack.pop();
        min.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min.peek();
    }
}
