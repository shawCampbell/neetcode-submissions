class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.vector = []
        self.res = []
        nums = sorted(candidates)

        def dfs(i=0, total=0):
            nonlocal nums
            if total == target:
                self.res.append(self.vector.copy())
                return
            if i == len(nums) or total > target:
                return
            self.vector.append(nums[i])
            dfs(i+1, total + nums[i])
            self.vector.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, total)
        dfs()
        return self.res