# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = fast = head

        for i in range(n):
            if not fast:
                return None
            fast = fast.next 

        dummy = ListNode()
        temp = dummy
        dummy.next = head
        while fast:
            temp = slow
            fast = fast.next
            slow = slow.next 

        temp.next = slow.next
        return dummy.next
            


        