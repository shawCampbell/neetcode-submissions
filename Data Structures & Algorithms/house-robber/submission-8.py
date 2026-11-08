class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_rob(x) = {
        #               max(max_rob(x-2), max_rob(x-1)) if x == l-1,
        #               else max(rob[x] + max_rob(x-2), max_rob(x-1))
        #              }
        max_one, max_two = 0, 0
        for n in nums:
            temp = max_two
            max_two = max(max_one + n, temp)
            max_one = temp
        return max_two