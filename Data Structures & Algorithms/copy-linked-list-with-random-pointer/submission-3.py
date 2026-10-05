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

        def copy_random(head):
            if not head:
                return None
            if head.random in new_nodes:
                new_rand = new_nodes[head.random]
            else:
                new_rand = Node(head.random.val)
                new_nodes[head.random] = new_rand
            if head in new_nodes:
                new_node = new_nodes[head]
            else:
                new_node = Node(head.val,None)
                new_nodes[head] = new_node
            new_node.random = new_rand
            new_node.next = copy_random(head.next)
            return new_node

        return copy_random(head)


