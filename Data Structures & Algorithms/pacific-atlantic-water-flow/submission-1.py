class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        ROWS, COLS = len(grid), len(grid[0])
        res = []

        seen= set()
        PAC=False
        ATL=False
        def dfs(r, c, h=float('inf')):
            nonlocal PAC
            nonlocal ATL
            if r == -1 or c == -1:
                # return ['PAC']
                PAC = True
                return
            if r == ROWS or c == COLS:
                # return ['ATL']
                ATL = True
                return
            if (grid[r][c] > h) or ((r, c) in seen):
                return #['NONE']
            
            h = grid[r][c]
            # ocs = []

            seen.add((r, c))
            dfs(r+1, c, h)
            dfs(r-1, c, h)
            dfs(r, c+1, h)
            dfs(r, c-1, h)
            # ocs.extend(dfs(r+1, c, h))
            # ocs.extend(dfs(r-1, c, h))
            # ocs.extend(dfs(r, c+1, h))
            # ocs.extend(dfs(r, c-1, h))

            # return ['PAC' if  'PAC' in ocs else 'NONE', 'ATL' if 'ATL' in ocs else 'NONE']

        for r in range(ROWS):
            for c in range(COLS):
                seen = set()
                PAC, ATL = False, False
                dfs(r, c)
                if PAC and ATL:#'PAC' in ocs and 'ATL' in ocs:
                    res.append([r, c])
        return res
