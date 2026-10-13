class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # breadth first search

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            area = 0
            while q:
                cur_r, cur_c = q.popleft()
                if (cur_r in range(ROWS) and
                    cur_c in range(COLS) and
                    grid[cur_r][cur_c] == 1):

                    area += 1
                    grid[cur_r][cur_c] = 0

                    q.append((cur_r+1, cur_c))
                    q.append((cur_r-1, cur_c))
                    q.append((cur_r, cur_c+1))
                    q.append((cur_r, cur_c-1))
            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, bfs(r,c))

        return max_area






        