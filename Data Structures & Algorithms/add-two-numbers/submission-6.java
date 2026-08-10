/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        // carry = 0
        int carry = 0;
        // sum = 0
        int sum = 0;
        // result
        ListNode result = new ListNode(0);
        ListNode first = result;

        // while l1 and l2 not null 
           while (true){
        //      if l1 not null 
                // if (l1 == null){
                //     break;
                // }
                if (l1 != null){
        //          sum += l1
                    sum = sum + l1.val;
        //          go to next node; 
                    if (l1 != null){
                        l1 = l1.next;
                    }
                }
        //      if l2 not null
                if (l2 != null){
        //          sum += l2
                    sum = sum + l2.val;
        //          got to next node
                    l2 = l2.next;
                    
                }
        //      sum += carry
                sum = sum + carry;
                //carry = 0;
        //      carry += carry(sum)
                carry = sum/10;
        //      put non carry part of sum in result
                result.val = sum%10;
        //      add node to result and go to it
                if (l1 == null && l2 == null){
                    break;
                }
                result.next = new ListNode(0);
                result = result.next;
        //      sum = 0 
                sum = 0;
           }

        // add carry to end of result 
        if(carry > 0){
            if(carry >= 10){
                result.next = new ListNode(carry%10);
                result = result.next;
                result.next = new ListNode(carry%10);
            }
            else{
                result.next = new ListNode(carry);
            }
        }
        return first;
        
    }
}
