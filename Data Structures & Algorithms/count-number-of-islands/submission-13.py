class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # union find

        ROWS = len(grid)
        COLS = len(grid[0])

        par = [i for i in range(ROWS*COLS)]
        rank = [1]*(ROWS*COLS)

        def indx(r, c):
            return r*COLS + c

        def find(n):
            if par[n] == n:
                return n
            return find(par[n])

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = par[p1]
            else:
                rank[p2] += rank[p1]
                par[p1] = par[p2]
            return True

        islands = 0
        direc = [[1, 0],[-1, 0],[0, 1],[0, -1],]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    n = indx(r,c)
                    for dr, dc in direc:
                        if not (r+dr in range(ROWS) and
                                c+dc in range(COLS) and
                                grid[r+dr][c+dc] == '1'):
                            continue

                        if union(n, indx(r+dr, c+dc)):
                            islands -= 1

        
        return islands




