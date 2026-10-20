class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cycle detection
        if not edges: 
            return True

        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2) 
            adj[n2].append(n1)

        visited = set()
        def dfs(n, prev):
            if (n in visited):
                return False
            if (not adj[n]):
                return True
            visited.add(n)
            for ne in adj[n]:
                if ne == prev:
                    continue
                if not dfs(ne, n):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

        