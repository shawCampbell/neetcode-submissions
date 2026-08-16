class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        heap = []
        for r in range(0, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            if r == len(nums) - 1 or r+1 >= k:
                while not(r - heap[0][1] <= k-1):  
                    heapq.heappop(heap)
                res.append(-heap[0][0])

        return res


            




            
            