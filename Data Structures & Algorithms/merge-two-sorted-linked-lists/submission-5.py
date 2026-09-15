# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(1)
        prev = root
        
        while list1 or list2:

            if list1 and list2 and list1.val <= list2.val:
                nxt = list1
                list1 = list1.next
            elif list2 and list1 and list2.val <= list1.val:
                nxt = list2 
                list2 = list2.next
            elif list1 and not list2:
                nxt = list1 
                list1 = list1.next
            elif list2 and not list1:
                nxt = list2
                list2 = list2.next
            prev.next = nxt
            prev = nxt
        prev.next = None
        return root.next


                