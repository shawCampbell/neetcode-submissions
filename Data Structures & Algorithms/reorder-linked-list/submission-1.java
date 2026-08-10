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
    public void reorderList(ListNode head) {

        ListNode ptr1 = head;
        ListNode ptr2 = head.next;

        if (ptr1.next == null){
            return;
        }

        while (ptr2 != null){
            if (ptr2.next == null){
                break;
            }
            ptr1 = ptr1.next;
            ptr2 = ptr2.next.next;
        }

        ptr1 = ptr1.next;
        ListNode ptrl = last(ptr1);
        ptr1 = this.reverse(ptr1);
        ptr1 = ptrl;

        // head.next = ptr1;
        // ptr1.next = null;
        
        while (ptr1 != null){
            // instert ptr1
            ListNode nextptr = ptr1.next;
            ptr1.next = head.next;
            head.next = ptr1;

            head = ptr1.next;
            ptr1 = nextptr;
        }

        head.next = null;
        
    }

    public static ListNode reverse(ListNode n){
        if (n.next == null){
            return n; // the last node
        }

        ListNode connect = reverse(n.next);
        n.next = null;
        connect.next = n;
        
        return n;

    }

    public ListNode last(ListNode n){
        if (n.next == null){
            return n;
        }
        return last(n.next);
    }

}
