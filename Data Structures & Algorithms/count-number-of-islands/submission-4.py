class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        direc = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        
        ones = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    ones.append((r, c))
        seen = set()
        def dfs(r, c):
            if not(r >= 0 and r < ROWS and c >= 0 and c < COLS) or grid[r][c] != "1" or (r,c) in seen:
                return
            seen.add((r,c))
            for dr in direc:
                dfs(r+dr[0], c+dr[1])


        islands = 0
        for r,c in ones:
            if (r,c) in seen:
                continue
            dfs(r, c)
            islands += 1

        return islands
        # adj = {}
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j] == "1":
        #             adj[(i, j)] = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]

        # nodes = set(adj.keys())
        # if not nodes:
        #     return 0
        # islands=0

        # def dfs(r, c):
        #     if not (r >= 0 and c >= 0 and r < ROWS and c < COLS) or grid[r][c] != "1" or (r,c) not in nodes:
        #         return
        #     nodes.remove((r, c))
        #     for i,j in adj[(r,c)]:
        #         dfs(i,j)

        # while nodes:
        #     n = next(iter(nodes))
        #     dfs(n[0], n[1])
        #     islands += 1
            
        # return islands




            
