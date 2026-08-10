class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i


























        # map = {}

        # for i,  n in enumerate(nums):
        #     complement = target - n
        #     if complement in map:
        #         return [map[complement], i]
        #     map[n] = i
        