class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        ROWS, COLS = len(grid), len(grid[0])
        res = []

        seen= set()
        def dfs(r, c, h=float('inf')):
            if r == -1 or c == -1:
                return ['PAC']
            if r == ROWS or c == COLS:
                return ['ATL']
            if (grid[r][c] > h) or ((r, c) in seen):
                return ['NONE']
            
            h = grid[r][c]
            ocs = []
            # print(r, c)
            seen.add((r, c))
            ocs.extend(dfs(r+1, c, h))
            ocs.extend(dfs(r-1, c, h))
            ocs.extend(dfs(r, c+1, h))
            ocs.extend(dfs(r, c-1, h))

            return ['PAC' if  'PAC' in ocs else 'NONE', 'ATL' if 'ATL' in ocs else 'NONE']

        for r in range(ROWS):
            for c in range(COLS):
                seen = set()
                ocs = dfs(r, c)
                if 'PAC' in ocs and 'ATL' in ocs:
                    res.append([r, c])
        return res
