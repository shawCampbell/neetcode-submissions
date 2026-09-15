# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        table = {
            (None, None): lambda n1,n2 : None,
            (0, None): lambda n1,n2: n1,
            (None, 0): lambda n1,n2: n2,
            (0, 0): lambda n1,n2: n1 if n1.val <= n2.val else n2
        }

        def incr(n):
            nonlocal list1
            nonlocal list2
            if list1 == n:
                list1 = list1.next
            else:
                list2 = list2.next
        
        prev = root = table[(0 if list1 else None, 0 if list2 else None)](list1, list2)
        if not root:
            return None
        incr(root)
        while table[(0 if list1 else None, 0 if list2 else None)](list1, list2):
            curr = table[(0 if list1 else None, 0 if list2 else None)](list1, list2)
            incr(curr)
            prev.next = curr
            prev = curr
        prev.next = None
        return root

        
        


                