class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(start):
            visited = set(start)
            q = deque(start)
            while q:
                for i in range(len(q)):
                    r, c = q.pop()
                    for dr, dc in direc:
                        nr, nc = r + dr, c + dc
                        if not (nr in range(ROWS) and
                                nc in range(COLS) and
                                heights[nr][nc] >= heights[r][c] and
                                (nr, nc) not in visited):
                                continue
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited

        left_top = []
        left_top.extend([(0,c) for c in range(COLS)])
        left_top.extend([(r,0) for r in range(ROWS)])
        left_top_set = bfs(left_top)

        right_bottom = []
        right_bottom.extend([(ROWS-1,c) for c in range(COLS)])
        right_bottom.extend([(r,COLS-1) for r in range(ROWS)])
        right_bottom_set = bfs(right_bottom)
        # print(right_bottom_set)

        res = []

        for c in left_top_set:
            # print(c)
            if c in right_bottom_set:
                res.append([c[0],c[1]])
        return res




                        

