class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums)-1
        m = 0

        while l < r:
            m = l + math.ceil( (r-l)/2 )

            if nums[m] <= target:
                l = m
            else:
                r = m - 1
            print(nums[l], nums[r], nums[m], sep=", ")

        return l if nums[l] == target else -1