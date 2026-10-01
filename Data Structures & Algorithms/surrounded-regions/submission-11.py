class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        notModify = set()
        
        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] == 'o' or
                board[r][c] == 'X'):
                return
            board[r][c] = 'o'
            # notModify.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'o':
                    board[r][c] = 'O'
                    continue
                if board[r][c] == 'O':
                    board[r][c] = 'X'


                
            
            
            






            