class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        max_robbery = [0]*len(nums)
        ready = [False]*len(nums)

        def dfs(n):
            if n > len(nums)-1:
                return 0
            if ready[n]:
                return max_robbery[n]
            
            max_r = 0
            for i in range(n+2 if n != 0 else n+1, len(nums)):
                max_r = max(dfs(i), max_r)
            max_robbery[n] = nums[n] + max_r
            ready[n] = True

            return nums[n] + max_r
        
        res = dfs(0)
        print(max_robbery)
        return res
