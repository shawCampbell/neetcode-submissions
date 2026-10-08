class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # subsets
        res = []
        COLS = len(nums)

        def dfs(i, temp):
            # print(i, temp)
            if i == COLS:
                res.append(temp.copy())
            else:
                dfs(i+1, temp)
                temp.append(nums[i])
                dfs(i+1, temp)
                temp.pop()

        dfs(0, [])
        return res
            
