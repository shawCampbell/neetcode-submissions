class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = len(nums)
        pref = [0]*l
        suff = [0]*l

        pref[0] = 1
        for i in range(1, l):
            pref[i] = nums[i-1]*pref[i-1]

        suff[l-1] = 1
        for i in range(l-2, -1, -1):
            suff[i] = nums[i+1]*suff[i+1]

        return [i*j for i,j in zip(pref, suff)]































        # a1 = [0 for i in range(len(nums))]
        # a1[0] = 1
        # for i in range(1, len(nums)):
        #     a1[i] = a1[i - 1]*nums[i - 1]

        # a2 = [0 for i in range(len(nums))]
        # a2[-1] = 1
        # for i in range(len(nums) - 2, -1, -1):
        #     a2[i] = a2[i + 1]*nums[i+1]

        # return [x*y for x,y in zip(a1, a2)]



        



        