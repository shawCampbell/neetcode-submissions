# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = dummy = ListNode()
        while l1 or l2 or carry:
            cur = ListNode()
            v1 = l1.val if l1 else 0
            l1 = l1.next if l1 else l1
            v2 = l2.val if l2 else 0
            l2 = l2.next if l2 else l2
            val = v1 + v2 + carry
            carry = val//10 
            val = val%10
            cur.val = val
            prev.next = cur
            prev = cur
        cur.next = None
        return dummy.next

        

