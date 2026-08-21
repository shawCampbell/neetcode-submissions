class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        maxR = 1
        incr = 1
        decr = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                decr += 1 
                maxR = max(maxR, decr)
            else:
                decr = 1 
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                incr += 1 
                maxR = max(maxR, incr)
            else:
                incr = 1
        return maxR