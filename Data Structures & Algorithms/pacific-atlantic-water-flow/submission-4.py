class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        ROWS, COLS = len(grid), len(grid[0])
        res = []

        seen= set()
        good_path = set()
        def dfs(r, c, h=float('inf')):
            
            if r == -1 or c == -1:
                return ['PAC']
                # PAC = True
                # return
            if r == ROWS or c == COLS:
                return ['ATL']
                # ATL = True
                # return
            if (grid[r][c] > h) or ((r, c) in seen):
                return ['NONE']
            if (r, c) in good_path:
                return ['PAC', 'ATL']
            
            h = grid[r][c]
            ocs = []

            seen.add((r, c))
            
            ocs.extend(dfs(r+1, c, h))
            ocs.extend(dfs(r-1, c, h))
            ocs.extend(dfs(r, c+1, h))
            ocs.extend(dfs(r, c-1, h))

            if 'PAC' in ocs and 'ATL' in ocs:
                good_path.add((r, c))

            return ['PAC' if  'PAC' in ocs else 'NONE', 'ATL' if 'ATL' in ocs else 'NONE']

        starts=[]
        for r in range(ROWS):
            for c in range(COLS):
                starts.append((r, c))
                # seen = set()
                # ocs = dfs(r, c)
                # if 'PAC' in ocs and 'ATL' in ocs:
                #     res.append([r, c])
        starts.sort(key = lambda x: -grid[x[0]][x[1]])
        for r,c in starts:
            seen = set()
            ocs = dfs(r, c)
            if 'PAC' in ocs and 'ATL' in ocs:
                res.append([r, c])
        return res
