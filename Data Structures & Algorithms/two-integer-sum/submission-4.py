class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, n in enumerate(nums):
            if (target - n) in seen: 
                return [seen[target - n], i]
            seen[n] = i























        # map = {}

        # for i,  n in enumerate(nums):
        #     complement = target - n
        #     if complement in map:
        #         return [map[complement], i]
        #     map[n] = i
        