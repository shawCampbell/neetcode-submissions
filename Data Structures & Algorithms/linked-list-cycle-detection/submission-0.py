# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    seen = set()
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head in self.seen:
            return True
        if not head:
            return False
        self.seen.add(head)
        return self.hasCycle(head.next)
        