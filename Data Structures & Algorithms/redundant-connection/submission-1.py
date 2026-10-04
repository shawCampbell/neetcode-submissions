class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        max_element = -1
        for n1, n2 in edges:
            max_element = max(max_element, n1, n2)

        par = [n for n in range(0, max_element+1)]
        # print(par)
        rank = [1]*(max_element+1)

        def get_parent(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def bad_edge(n1, n2):
            p1, p2 = get_parent(n1), get_parent(n2) 
            if p1 == p2:
                return True
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return False

        bad = set()
        for e in edges:
            if bad_edge(e[0], e[1]): bad.add(tuple(e))
        
        for e in edges[::-1]:
            if tuple(e) in bad: return e
            
            
