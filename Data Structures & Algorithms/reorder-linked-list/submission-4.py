# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next 
        
        prev = slow.next
        curr = prev.next
        slow.next = prev.next = None 

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp 

        curr = head

        while prev:
            temp_curr = curr.next
            temp_prev = prev.next

            curr.next = prev
            prev.next = temp_curr

            prev = temp_prev
            curr = temp_curr


        
        







