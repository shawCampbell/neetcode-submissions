class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        path = []
        def dfs(r, c, i):
            # print(r,c,path, (r,c) in path)
            if i == len(word):
                return True
            if  (not (r in range(ROWS) and c in range(COLS)) or 
                ((r,c) in path)):
                return False
            dirs = [[0, 1],[0, -1],[1, 0],[-1, 0]]
            for dr,dc in dirs:
                path.append((r,c))
                if (board[r][c] == word[i]) and dfs(r+dr, c+dc, i+1): return True
                path.pop()
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
