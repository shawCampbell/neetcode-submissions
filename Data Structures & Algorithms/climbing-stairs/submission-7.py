class Solution:
    def climbStairs(self, n: int) -> int:

        # dynamic programming, top-down
        cache = {
            1: 1,
            2: 2
        }
        total = 0
        def dfs(n):
            if n in cache:
                return cache[n]
            res = dfs(n-1) + dfs(n-2)
            cache[n] = res
            return res

        return dfs(n)

