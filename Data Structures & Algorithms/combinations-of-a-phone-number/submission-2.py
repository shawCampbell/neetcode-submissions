class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []
        temp = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(temp))
                return
            for l in letters[digits[i]]:
                temp.append(l)
                dfs(i+1)
                temp.pop()
        if not digits: return []
        dfs(0)
        return res
            
