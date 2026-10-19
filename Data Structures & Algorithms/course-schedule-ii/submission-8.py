class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort

        # build adjaceny list
        adj = {c:[[],0] for c in range(numCourses)}
        for c,p in prerequisites:
            adj[c][0].append(p)

        res = []

        def topological_sort(c):
            print(c,adj[c][1])
            if adj[c][1] == 2:
                return True
            if adj[c][1] == 1:
                return False

            adj[c][1] = 1
            for p in adj[c][0]:
                if not topological_sort(p):
                    return False
            
            adj[c][1] = 2
            res.append(c)
            return True

        for c in range(numCourses):
            if not topological_sort(c):
                return []

        return res

            
            