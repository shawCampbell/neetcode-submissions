class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # union find

        ROWS, COLS = len(grid), len(grid[0])
        par = [n for n in range(ROWS*COLS)]
        rank = [1]*(ROWS*COLS)

        def indx(r, c):
            return r*COLS + c

        def find(n):
            if n == par[n]:
                return n
            return find(par[n])

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = par[p1]
            else:
                rank[p2] += rank[p1]
                par[p1] = par[p2]

        # instantiate union find data structure (rank-based)
        ones_exist = False
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if not (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1):
                        continue
                ones_exist = True
                for dr,dc in direc:
                    if (r+dr in range(ROWS) and
                        c+dc in range(COLS) and
                        grid[r+dr][c+dc] == 1): 
                        union(indx(r, c), indx(r+dr, c+dc))

        return max(rank) if ones_exist else 0





        