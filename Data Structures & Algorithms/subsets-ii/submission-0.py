class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.vector = []
        self.res = []
        nums.sort()
        def dfs(i=0):
            if i == len(nums):
                self.res.append(self.vector.copy())
            else:
                self.vector.append(nums[i])
                dfs(i+1)
                self.vector.pop()
                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1
                dfs(i+1)
        dfs()
        return self.res