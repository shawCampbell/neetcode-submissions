class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l,r = 0, len(nums)-1
        
        while nums[l] + nums[r] != target:
            if nums[l]+nums[r] < target:
                l += 1
            elif nums[l]+nums[r] > target:
                r -= 1
        return [l+1,r+1]