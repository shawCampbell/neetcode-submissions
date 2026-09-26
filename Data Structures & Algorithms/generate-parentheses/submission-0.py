class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def dfs(o=1, c=0, s='('):
            nonlocal n
            if o == n and c == n:
                self.res.append(s)
                return
            if o < n:
                t = s+'('
                dfs(o+1, c, t)
                # s = s[:len(s)-1]
            if c < o:
                t = s+')'
                dfs(o, c+1, t)
        dfs()
        return self.res
            

