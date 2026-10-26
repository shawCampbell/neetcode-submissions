class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.heap = nums[-k:] if (len(nums) > k) else nums
        # print(self.heap)
        heapq.heapify(self.heap)
        self.k = k 

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
