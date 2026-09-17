class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for fast in range(1, len(nums)):
            slow = 0
            while fast < len(nums):
                if nums[slow] == nums[fast]:
                    return nums[slow]
                slow += 1
                fast += 1
        