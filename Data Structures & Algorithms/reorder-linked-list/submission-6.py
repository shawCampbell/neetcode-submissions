# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find midpoint
        p1 = p2 = head
        while p2 and p2.next:
            p2 = p2.next.next
            if p2:
                p1 = p1.next
        # print(p1.val)
        prev = None
        cur = p1.next
        p1.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # print(prev.next.next)
        # print(prev.next.next)
        start = head
        while start and prev:
            start_nxt = start.next
            prev_nxt = prev.next
            start.next = prev
            prev.next = start_nxt
            prev = prev_nxt
            start = start_nxt
        # print(head.next.next.next.next)
        # return head


