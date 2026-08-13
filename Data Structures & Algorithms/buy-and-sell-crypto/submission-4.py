class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        l = 0
        max = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] > max:
                max = prices[r] - prices[l]
            if prices[r] <= prices[l]:
                l = r
                r += 1
        return max




