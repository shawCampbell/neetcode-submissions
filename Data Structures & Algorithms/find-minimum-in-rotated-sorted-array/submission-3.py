class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] < nums[-1]:
            return nums[0]
        # 1 2 3 4 5 6
        # 2 3 4 5 6 1
        # 3 4 5 6 1 2
        # 4 5 6 1 2 3
        
        # I I I D D D

        # n[0] > x and n[5] > x
        # n[0] > n[5] >= x
        m=0
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l)//2
            print(l, r, m, sep=", ")
            if nums[0] > nums[m]:
                r = m
            else:
                l = m + 1
        print(l, r, m, sep=", ")

        return nums[l]