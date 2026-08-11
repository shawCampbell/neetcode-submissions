class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # l = 0
        # r = len(nums) -1
        # middle = 0

        # while l <= r:
        #     middle = l + (r - l)//2

        #     if target < nums[middle]:
        #         r = middle - 1
        #     elif target > nums[middle]:
        #         l = middle + 1
        #     else:
        #         return middle

        # return -1
        # c = 0

        def binary_search(nums, l, r, target):
            # nonlocal c 
            # c += 1
            # if c == 5:
            #     return -1
            middle = l + (r - l)//2
            # print(nums[l:r], l, r, middle, sep=", ")
            if (r <= l):
                return middle if(nums[middle] == target) else -1
            if (nums[middle] == target):
                return middle
            if (nums[middle] < target):
                # print("bigger")
                return binary_search(nums, middle + 1, r, target)

            return binary_search(nums, l, middle - 1, target)
            # print("smaller")

        return binary_search(nums, 0, len(nums) - 1, target)

