class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = []
        res = []

        def dfs(i=0):
            if i == len(nums):
                res.append(temp.copy())
                return
            j = i
            while j+1 < len(nums) and nums[j] == nums[j+1]:
                j += 1
            dfs(j+1)

            temp.append(nums[i])
            dfs(i+1)
            temp.pop()

        dfs()
        return res