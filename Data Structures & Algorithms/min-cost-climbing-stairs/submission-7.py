class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[0], cost[1]
        cost.append(0)

        for i in range(2, len(cost)):
            temp = two
            two = cost[i] + min(one, two)
            one = temp

        return two
        