class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # breadth first search
        ROWS, COLS = len(grid), len(grid[0])
        
        # num_ones = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             num_ones += 1

        found_ones = 0
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                root = (i,j)
                # if found_ones < num_ones:
                #     return islands
                if grid[i][j] == '0':
                    continue 
                islands += 1
                q = deque()
                q.append(root)
                while q:
                    r, c = q.popleft()
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == '1':
                        grid[r][c] = '0'
                        # found_ones += 1
                        q.append((r+1, c))
                        q.append((r-1, c))
                        q.append((r, c+1))
                        q.append((r, c-1))
        return islands




