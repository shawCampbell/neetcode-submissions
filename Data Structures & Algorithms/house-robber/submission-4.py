class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums.insert(0, 0)
        # max_robbery = [0]*len(nums)
        # ready = [False]*len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            nums[i] += max(nums[i+2] if i+2 in range(len(nums)) else 0,
                           nums[i+3] if i+3 in range(len(nums)) else 0)
        print(nums)
        return max(nums[0], nums[1]) if 1 in range(len(nums)) else nums[0]

