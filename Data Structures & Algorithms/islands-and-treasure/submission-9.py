class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multisource bfs
        ROWS, COLS = len(grid), len(grid[0])
        treasures = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasures.append((r,c,1))
        
        q = deque()
        for t in treasures:
            q.append(t)
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for i in range(len(q)):
                r,c,dist = q.popleft()
                for dr,dc in direc:
                    nr, nc = r + dr, c + dc
                    if not (nr in range(ROWS) and 
                            nc in range(COLS) and
                            grid[nr][nc] == 2**31 - 1):
                            continue
                    grid[nr][nc] = dist 
                    q.append((nr, nc, dist+1))
        