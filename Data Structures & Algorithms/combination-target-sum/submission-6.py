class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.vector = []
        self.res = []

        def dfs(i=0, total=0):
            if total == target:
                self.res.append(self.vector.copy())
                return
            if i > len(nums) - 1 or total > target:
                return
            self.vector.append(nums[i])
            dfs(i, total+nums[i])
            self.vector.pop()
            dfs(i+1, total)
        dfs()
        return self.res
