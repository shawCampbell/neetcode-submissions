# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()
        carry = 0
        while l1 or l2 or carry != 0:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val

            s = l1_val + l2_val + carry
            val = (s)%10
            carry = s//10

            cur = ListNode(val)
            prev.next = cur
            prev = cur

            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next 
        return dummy.next
        