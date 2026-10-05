# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.get_length(head)
        target = l - n
        count = 0

        if target < 0:
            return []

        cur = dummy = ListNode()
        cur.next = head
        while count < target - 1:
            cur = cur.next
            count += 1
        cur.next = cur.next.next
        
        return dummy.next


    def get_length(self, head: ListNode) -> int:
        count = 1
        while head:
            head = head.next
            count += 1
        return count


