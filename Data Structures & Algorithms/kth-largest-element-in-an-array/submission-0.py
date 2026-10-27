class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-e for e in nums]
        heapq.heapify(nums)

        cur = 0
        for i in range(k):
            cur = heapq.heappop(nums)

        return -cur