# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        start = end = head 
        l = 1
        while end:
            end = end.next
            l += 1 

        target = l - n
        # print(l, target, sep=", ")
        if target > l-1:
            return None

        prev = dummy
        for i in range(1, target):
            prev = start
            start = start.next 

        prev.next = start.next
        return dummy.next
            


        