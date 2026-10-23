class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {n: 0 for n in nums}
        for n in nums:
            freq[n] += 1
            if freq[n] > 1:
                return True
        return False
        