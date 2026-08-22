class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        par = 0 if nums[0]%2==0 else 1
        for i in range(1, len(nums)):
            if nums[i]%2 == 0 and par == 0:
                return False
            elif nums[i]%2 != 0 and par == 1:
                return False
            par = 0 if nums[i]%2==0 else 1

        return True