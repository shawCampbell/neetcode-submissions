class Solution {
    public boolean isValid(String s) {
        // stack
        // String[] sArr = s.split("");
        // Stack<String> br = new Stack<>();
        // String state = "";

        // if (sArr.length%2 != 0){
        //     return false;
        // }

        // for (int i = 0; i <= sArr.length - 1; i++){
        //     if(sArr[i].equals("(")||sArr[i].equals("[")||sArr[i].equals("{")){
        //         br.push(sArr[i]);
        //         state = sArr[i];
        //     }
        //     else if (get(state)==get(sArr[i])){
        //         //throw new IllegalArgumentException(sArr[i]);
        //         br.pop();
        //         if (!br.empty()){
        //             state = br.pop();
        //             br.push(state);
        //         }
        //         else{
        //             state = "";
        //         }
        //     }
        // }

        // if (br.empty() && flag){
        //     return true;
        // }
        // return false;

        // System.out.println("Hey");
        // return false;

        String[] sArr = s.split("");
        Stack<String> br = new Stack<>();

        for (int i = 0; i <= sArr.length - 1; i++){
            System.out.println("for" + Integer.toString(i));
            System.out.println("check "+ sArr[i]);
            if (sArr[i].equals("(")||sArr[i].equals("[")||sArr[i].equals("{")){
                
                br.push(sArr[i]);
                System.out.println("push " +br.toString());
            }
            else{
                System.out.println("check if empty: " + br.toString());
                if(br.empty()){
                    return false;
                }
                String popped = br.pop();
                System.out.println("cmp " + sArr[i] +", " + popped + " to " + Boolean.toString((get(sArr[i])!=get(popped))) + " with " + br.toString());
                if (get(sArr[i])!=get(popped)){
                    return false;
                }
                // System.out.println("eval " +br.toString());
                // if(br.empty()){
                //     return false;
                // }
                // int j = i;
                // while (!br.empty() && j <= sArr.length-1){
                //     String popped = br.pop();
                //     System.out.println("comp "+ sArr[j]+" "+popped);
                //     if (!(get(sArr[j])==get(popped))){
                //         System.out.println(sArr[j]);
                //         System.out.println(br.toString());
                //         return false;
                //     }
                //     j++;
                // }
                // System.out.println("i=j "+Integer.toString(j));
                // i=j-1;
            }
        }

        System.out.println(br.toString());

        if (br.empty()){
            return true;
        }

        return false;

    }

    public static int get(String s){
        // throw new IllegalArgumentException(s);
        if (s.equals("")){
            return -1;
        }
        switch(s.charAt(0)){
            case '(':
                return 0;
                //break;
            case ')':
                return 0;
                //break;
            case '[':
                return 1;
                //break;
            case ']':
                return 1;
                //break;
            case '{':
                return 2;
                //break;
            case '}':
                return 2;
                //break;
            default:
                return -1;
                //break;
        }
    }
}
