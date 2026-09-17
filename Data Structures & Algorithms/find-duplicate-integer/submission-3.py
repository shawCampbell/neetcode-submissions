class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # find one before start of cycle
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 


        # find start of cycle
        cur = 0
        while True:
            slow = nums[slow]
            cur = nums[cur]
            if cur == slow:
                break

        return cur
        
        