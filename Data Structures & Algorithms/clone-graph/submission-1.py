"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_nodes = {
            None: None
        }

        def dfs(root):
            if root in new_nodes:
                return new_nodes[root]

            new_root = Node(root.val)
            new_nodes[root] = new_root

            if new_root:
                for ne in root.neighbors:
                    new_root.neighbors.append(dfs(ne))

            return new_root

        return dfs(node)
