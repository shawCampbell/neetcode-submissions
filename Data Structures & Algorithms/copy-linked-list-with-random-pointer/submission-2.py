"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = {None: None}

        cur = head
        prev = dummy = Node(0)
        while cur:
            new_cur = Node(cur.val, None, cur.random)
            new_nodes[cur] = new_cur
            prev.next = new_cur
            prev = new_cur
            cur = cur.next
        prev.next = None

        cur = dummy.next
        while cur:
            cur.random = new_nodes[cur.random]
            cur = cur.next

        return dummy.next
        

