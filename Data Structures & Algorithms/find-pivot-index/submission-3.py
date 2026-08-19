class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)):
            ls = 0
            for l in nums[:i]:
                ls += l
            rs = 0
            if i+1 == len(nums):
                rs = 0
            else:
                for r in nums[i+1:]:
                    rs += r
                print(ls, rs)
            if ls == rs:
                return i 
        return -1

        