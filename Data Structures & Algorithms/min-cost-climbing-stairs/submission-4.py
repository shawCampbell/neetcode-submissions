class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # recursively
        # cost.insert(0, 0)
        # cost.append(0)

        # l = len(cost)
        # min_costs = [0]*(l)
        # ready = [False]*(l)

        # def min_cost(s):
        #     if s < 0:
        #         return 0
        #     if ready[s]:
        #         return min_costs[s]
            
        #     min_c = cost[s] + min(min_cost(s-1), min_cost(s-2))
        #     min_costs[s] = min_c
        #     ready[s] = True
        #     return min_c
         
        # min_cost(l-1)
        # return min_costs[-1]

        # iteratively
        cost.insert(0,0)
        cost.append(0)
        ready = [False]*len(cost)
        m_costs = [float('inf')]*len(cost)
        m_costs[0] = 0

        for n in range(1, len(cost)):
            for s in range(1, 3):
                if n - s >= 0:
                    m_costs[n] = min(m_costs[n], cost[n] + m_costs[n-s])
        print(m_costs)
        return m_costs[-1]


            



        