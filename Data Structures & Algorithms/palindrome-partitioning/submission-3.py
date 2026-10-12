class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s = [c for c in s]
        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        res = []
        temp = []
        def dfs(l=0, r=0):
            if r >= len(s):
                if l == r:
                    res.append(temp.copy())
                return

            if palindrome(l,r):
                temp.append("".join(s[l:r+1]))
                dfs(r+1, r+1)
                temp.pop()

            dfs(l,r+1)
                   
        dfs()
        return res
            
            
