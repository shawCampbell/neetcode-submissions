class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0, 0)
        cost.append(0)
        # print(cost)

        l = len(cost)
        min_costs = [0]*(l)
        ready = [False]*(l)

        def min_cost(s):
            if s < 0:
                return 0
            if ready[s]:
                return min_costs[s]
            
            min_c = cost[s] + min(min_cost(s-1), min_cost(s-2))
            min_costs[s] = min_c
            ready[s] = True
            return min_c
         
        min_cost(l-1)
        return min_costs[-1]

            



        