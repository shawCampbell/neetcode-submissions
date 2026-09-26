class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.vector = []
        self.res = []
        self.chosen = [False for n in nums]
        def dfs(i=0):
            nonlocal nums
            if len(self.vector) == len(nums):
                self.res.append(self.vector.copy())
            for i in range(len(nums)):
                if self.chosen[i]: continue
                self.vector.append(nums[i])
                self.chosen[i] = True
                dfs(i)
                self.chosen[i] = False
                self.vector.pop()
        dfs()
        return self.res
                