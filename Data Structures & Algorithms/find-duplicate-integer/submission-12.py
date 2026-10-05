class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's algorithm
        def nxt(i):
            return nums[i]

        slow = fast = 0
        while True:
            slow = nxt(slow)
            fast = nxt(nxt(fast))
            if fast == slow:
                break
        
        start1, start2 = 0, slow
        while True:
            start1, start2 =  nxt(start1), nxt(start2)
            if start1 == start2:
                return start1


