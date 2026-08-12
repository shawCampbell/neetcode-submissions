class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 1 2 3 4 5 6
        # 6 1 2 3 4 5
        # 5 6 1 2 3 4
        # 4 5 6 1 2 3
        # 3 4 5 6 1 2

        # min is at l

        def binary_search(l, r):
            nonlocal nums 
            nonlocal target
            m = 0
            while l <= r:
                m = l + (r - l)//2
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    return m
            return -1 
        
                # find min or privot 
        m = 0
        if (nums[0] <= nums[-1]):
            return binary_search(0, len(nums) - 1)
        else:
            l, r = 0, len(nums)-1
            while l < r:
                m = l + (r - l)//2
                print(l, r, m, nums)

                if nums[0] <= nums[m]: # in the left set
                    l = m + 1
                else: # in the right set
                    r = m

        return max(binary_search(0, l), binary_search(l, len(nums) - 1))

        
