class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        com = []
        def dfs(i, s):
            if s == target:
                res.append(com.copy())
                return
            if s > target or i == len(nums):
                return
            com.append(nums[i])
            dfs(i, s+nums[i])
            com.pop()
            dfs(i+1, s)

        dfs(0, 0)
        return res


