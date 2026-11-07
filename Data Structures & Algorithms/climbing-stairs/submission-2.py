class Solution:
    def climbStairs(self, n: int) -> int:
        # count number of valid solns

        # count(n) = {
        #               0 if n < 0,
        #               1 if n == 0,
        #               else count(n - 1) + count(n - 2)
        #            }

        ready = [False]*(n+1)
        count_arr = [0]*(n+1)

        # recursively
        def count(n):
            if ready[n]:
                return count_arr[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            res = count(n-1) + count(n-2)
            ready[n] = True
            count_arr[n] = res
            return res

        return count(n)







