class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(r,c):
            if grid[r][c] == 0:
                return 0
            area = 1
            d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            seen.add((r, c))
            for dr, dc in d:
                new_r, new_c = r+dr, c+dc
                
                if (new_r in range(ROWS) and 
                    new_c in range(COLS) and
                    (new_r, new_c) not in seen):

                        area += dfs(new_r, new_c)
            return area
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea


        # ROWS, COLS = len(grid), len(grid[0])
        # maxArea = 0
        # seen = set()

        # def bfs(r, c):
        #     area = 0

        #     d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        #     q = deque()
        #     q.append((r, c))
        #     seen.add((r, c))
        #     while q:
        #         cur_r, cur_c = q.popleft()
        #         # seen.add((cur_r, cur_c))
        #         # print(cur_r, cur_c)
        #         area += 1
        #         for dr, dc in d:
        #             new_r, new_c = cur_r+dr, cur_c+dc
        #             if (new_r in range(ROWS) and 
        #                 new_c in range(COLS) and 
        #                 grid[new_r][new_c] == 1 and
        #                 (new_r, new_c) not in seen):

        #                 q.append((new_r, new_c))
        #                 seen.add((new_r, new_c))
        #     return area

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1 and (r,c) not in seen:
        #             maxArea = max(maxArea, bfs(r, c))
        # return maxArea
