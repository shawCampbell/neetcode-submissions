class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # freq = {}

        # for num in nums:
        #     if num in freq:
        #         return True
        #     else:
        #         freq[num] = 1 
        # return False

        create_set = set(nums)
        return len(create_set) != len(nums)