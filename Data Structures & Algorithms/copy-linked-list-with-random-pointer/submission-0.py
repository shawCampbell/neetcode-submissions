"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    seen = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        prev = dummy = Node(0)
        copies = {}

        curr = head
        while curr:
            new_node = Node(curr.val, None, curr.random)
            copies[curr] = new_node
            prev.next = new_node
            prev = new_node
            curr = curr.next 
        prev.next = None

        prev = dummy
        curr = dummy.next
        while curr:
            curr.random = None if not curr.random else copies[curr.random]
            curr = curr.next

        return dummy.next







            







        
        

        