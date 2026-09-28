class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        if not grid:
            return 0

        seen = set()
        def bfs(r, c):
            direc = [[1,0], [-1,0], [0,1], [0,-1]]
            q = deque()
            q.append((r, c))
            while q:
                r,c = q.pop()
                seen.add((r,c))
                for dr,dc in direc:
                    if r+dr >= 0 and r+dr < ROWS and c+dc >= 0 and c+dc < COLS and grid[r+dr][c+dc] == "1" and (r+dr, c+dc) not in seen:
                        q.append((r+dr, c+dc))

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in seen or grid[i][j] == "0":
                    continue
                islands += 1
                bfs(i, j)                       

        return islands
        




            
