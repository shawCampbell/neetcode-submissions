class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if (s1 - s2) != 0:
                heapq.heappush(stones, min(s1, s2) - max(s1, s2))

        return -stones[0] if stones else 0
