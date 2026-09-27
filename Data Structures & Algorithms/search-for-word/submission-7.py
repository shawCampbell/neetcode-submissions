class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])

        self.seen = set()
        
        def dfs(r, c, i=0):
            if i == len(word):
                return True

            if (r < 0 or
                c < 0 or
                r >= self.ROWS or
                c >= self.COLS or
                word[i] != board[r][c] or
                (r,c) in self.seen):

                return False

            self.seen.add((r, c))   
            res = (dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1))
            self.seen.remove((r, c))
            return res

        for r in range(self.ROWS):
            for c in range(self.COLS):
                res = dfs(r, c)
                if res:
                    return True
        return False


