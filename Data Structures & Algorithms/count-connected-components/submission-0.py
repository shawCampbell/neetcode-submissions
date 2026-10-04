class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for i1, i2 in edges:
            adj[i1].append(i2)
            adj[i2].append(i1)

        components = 0
        visited = set()
        def dfs(i, prev):
            if i in visited or i == prev:
                return
            visited.add(i)
            for j in adj[i]:
                dfs(j, i)
        
        i = -1
        while len(visited) != n:
            i += 1
            if i in visited:
                continue
            dfs(i, -1)
            components += 1

        return components
