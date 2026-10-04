# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = p2 = head
        while p2:
            for i in range(2):
                if p2:
                    p2 = p2.next
                if p2 == p1:
                    return True
            p1 = p1.next
        return False

        