# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        l, r = head, head.next

        while r:
            l = l.next
            for i in range(2):
                if r:
                    r = r.next
                if r == l:
                    return True
        return False
        