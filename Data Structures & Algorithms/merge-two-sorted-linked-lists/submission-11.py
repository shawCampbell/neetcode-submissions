# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = root = ListNode()
        def merge():
            nonlocal list1
            nonlocal list2
            nonlocal root
            if not list1 and not list2:
                return
            v1 = list1.val if list1 else float('inf')
            v2 = list2.val if list2 else float('inf')
            if v1 <= v2:
                temp = list1
                list1 = list1.next                
            else:
                temp = list2
                list2 = list2.next
            root.next = temp
            root = temp
            merge()
        merge()
        return dummy.next
            
        # prev = dummy = ListNode()
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         cur = list1
        #         list1 = list1.next
        #     else:
        #         cur = list2
        #         list2 = list2.next
        #     prev.next = cur
        #     prev = cur
        
        # if list1:
        #     prev.next = list1
        # elif list2:
        #     prev.next = list2

        # return dummy.next
