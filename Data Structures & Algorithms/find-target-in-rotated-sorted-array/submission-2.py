class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l)//2

            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m 
        pivot = l

        def binary_search(l, r):
            if not l <= r:
                return l if nums[l] == target else -1

            while l <= r:
                m = l + (r - l)//2

                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    return m
            return -1

        return max(binary_search(0, pivot-1), binary_search(pivot, len(nums)-1))