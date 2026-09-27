class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        vector = []
        d_map = {
            1: [],
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y', 'z']
        }
        
        ds = [d_map[int(c)] for c in digits]
        # print(ds)

        def dfs(dig=0):
            if len(vector) == len(ds) or dig == len(ds):
                if vector:
                    res.append("".join(vector.copy())) 
                return
            for l in ds[dig]:
                vector.append(l)
                dfs(dig+1)
                vector.pop()
                # dfs(dig+1)
        dfs()
        # print(res)
        return res



                
            
            
            