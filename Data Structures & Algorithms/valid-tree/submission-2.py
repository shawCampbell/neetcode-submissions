class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        adj = {n:[] for n in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def valid_tree(n):
            if n in visited:
                return False
            visited.add(n)
            if not adj[n]:
                return True
            for ne in adj[n]:
                adj[ne].remove(n)
                if not valid_tree(ne): return False
            return True
        return valid_tree(n1) and len(visited) == n

