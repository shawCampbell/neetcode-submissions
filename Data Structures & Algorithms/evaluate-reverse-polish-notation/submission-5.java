class Solution {
    public int evalRPN(String[] tokens) {

        Stack<String> st = new Stack<>();
        
        for (String t : tokens){
            if (!"*+-/".contains(t)){
                System.out.println(t);
                st.push(t);
            }
            else{
                int n2 = Integer.parseInt(st.pop());
                int n1 = Integer.parseInt(st.pop());
                //st.push(operate(n1, n2, t));
                Integer computed;
                if (t.equals("*")){
                    computed = n1*n2;
                }
                else if(t.equals("+")){
                    computed = n1+n2;
                }
                else if(t.equals("-")){
                    computed = n1-n2;
                }
                else if(t.equals("/")){
                    computed = n1/n2;
                }
                else{
                    System.out.println("not valid operator");
                    computed = -1;
                }
                st.push(computed.toString());
            }
        }

        return Integer.parseInt(st.pop());
    }

}
