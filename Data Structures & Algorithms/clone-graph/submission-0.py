"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        generate_map_seen = set()
        new_nodes = {}
        def generate_map(n):
            if n in generate_map_seen:
                return
            generate_map_seen.add(n)
            new_nodes[n] = Node(n.val)
            for ne in n.neighbors:
                generate_map(ne)

        create_new_map_seen = set()
        def create_new_graph(n):
            if n in create_new_map_seen:
                return new_nodes[n]
            create_new_map_seen.add(n)
            for ne in n.neighbors:
                new_nodes[n].neighbors.append(create_new_graph(ne))
            return new_nodes[n]
        
        generate_map(node)
        return create_new_graph(node)



            