class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        adj = {}
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    adj[(i, j)] = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]

        nodes = set(adj.keys())
        if not nodes:
            return 0
        islands=0
        def dfs(r, c):
            if not (r >= 0 and c >= 0 and r < ROWS and c < COLS) or grid[r][c] != "1" or (r,c) not in nodes:
                return
            nodes.remove((r, c))
            for i,j in adj[(r,c)]:
                dfs(i,j)

        while nodes:
            n = next(iter(nodes))
            dfs(n[0], n[1])
            islands += 1
            
        return islands




            
