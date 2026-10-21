class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # self.largest = max(nums)
        heapq.heapify(nums)
        # print(nums, type(nums))
        self.heap = nums
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # self.largest = max(self.largest, val)
        return self.heap[0]

        


        
