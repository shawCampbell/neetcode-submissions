class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # depth first search

        # create adjacency list
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for ne in adj[n]:
                dfs(ne)

        components = 0
        for n in range(n):
            if n in visited:
                continue
            components += 1
            dfs(n)
        return components