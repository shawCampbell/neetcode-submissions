# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rev(head, first=False):

            if not head.next:
                return head, head

            n, last = rev(head.next)
            n.next = head

            if first:
                head.next = None

            return head, last

        if not head:
            return head
        _, last = rev(head, True)
        return last

