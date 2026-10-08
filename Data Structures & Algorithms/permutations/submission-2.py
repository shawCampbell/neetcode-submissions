class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def dfs():
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs()
                temp.pop()
        dfs()
        return res
