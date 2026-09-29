class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        numFresh = 0

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    numFresh += 1

        def propagate(r, c):
            nonlocal numFresh
            if (r in range(ROWS) and c in range(COLS)) and grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))
                numFresh -= 1
                return True
            return False

        # change = True
        while q and numFresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                # change = (
                propagate(r+1,c) #or
                propagate(r-1,c) #or
                propagate(r,c+1) #or
                propagate(r,c-1) #)
            time += 1

        return time if numFresh == 0 else -1
