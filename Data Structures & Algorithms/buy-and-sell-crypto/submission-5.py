class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxRes = -float('infinity')

        p1, p2 = 0, 0

        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 = p2
            else:
                maxRes = max(maxRes, prices[p2] - prices[p1])
            p2 += 1

        return maxRes