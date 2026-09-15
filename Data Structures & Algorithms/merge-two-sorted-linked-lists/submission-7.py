# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        prev = root = ListNode(1)

        while list1 or list2:
            v1 = float('infinity') if not list1 else list1.val
            v2 = float('infinity') if not list2 else list2.val

            if v1 <= v2:
                prev.next = list1
                prev = list1
                list1 = list1.next 
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        return root.next

        
        


                