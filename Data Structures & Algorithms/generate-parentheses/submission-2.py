class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []

        def dfs(open, close):
            if close == n and open == n:
                res.append(''.join(temp))
                return
            if open < n:
                temp.append('(')
                dfs(open+1, close)
                temp.pop()
            if open > close:
                temp.append(')')
                dfs(open, close+1)
                temp.pop()
        dfs(0, 0)
        return res