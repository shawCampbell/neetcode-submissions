class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # union-find
        ROWS, COLS = len(grid), len(grid[0])

        # create adjaceny list
        adj = {}
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0':
                    continue
                direc = [[1,0],[-1,0],[0,1],[0,-1]]
                adj[(r,c)] = []
                for dr,dc in direc:
                    if (r+dr in range(ROWS) and
                        c+dc in range(COLS) and
                        grid[r+dr][c+dc] == '1'):
                        adj[(r,c)].append((r+dr, c+dc))

        parents = [[(r, c) for c in range(COLS)] for r in range(ROWS)]
        rank = [[1 for c in range(COLS)] for r in range(ROWS)]

        def find(r, c):
            if parents[r][c] == (r,c):
                return parents[r][c]
            return find(parents[r][c][0], parents[r][c][1])

        islands = len(adj.keys())
        def union_find(n1, n2):
            nonlocal islands
            p1, p2 = find(n1[0], n1[1]), find(n2[0], n2[1])
            if p1 == p2:
                return
            if rank[p1[0]][p1[1]] > rank[p2[0]][p2[1]]:
                rank[p1[0]][p1[1]] += rank[p2[0]][p2[1]]
                parents[p2[0]][p2[1]] = parents[p1[0]][p1[1]] 
                islands -= 1
            else:
                rank[p2[0]][p2[1]] += rank[p1[0]][p1[1]]
                parents[p1[0]][p1[1]] = parents[p2[0]][p2[1]]
                islands -= 1
        
        for n1 in adj.keys():
            for n2 in adj[n1]:
                if not n2:
                    islands += 1
                    continue
                union_find(n1, n2)
        
        # print(adj)
        # print()
        # for r in parents:
        #     print(r)
        # print()
        # for r in grid:
        #     print(r)
        return islands

                

        
        




