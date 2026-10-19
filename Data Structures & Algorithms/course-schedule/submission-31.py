class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # construct adjaceny list
        adj = {c:[[], 0] for c in range(numCourses)}
        for c, p in prerequisites:
            adj[c][0].append(p)

        # Topological sort - directed graph

        topological_sort = []

        def dfs(c):
            if adj[c][1] == 2:
                return 
            if adj[c][1] == 1:
                return
            adj[c][1] = 1
            for p in adj[c][0]:
                # print(c, p, adj[p][1])
                if adj[p][1] == 1:
                    return 
                dfs(p)
            topological_sort.append(c)
            adj[c][1] = 2

        for c in adj.keys():
            dfs(c)

        print(topological_sort)
        return len(topological_sort) == numCourses














