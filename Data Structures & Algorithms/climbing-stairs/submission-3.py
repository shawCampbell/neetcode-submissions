class Solution:
    def climbStairs(self, n: int) -> int:
        # count number of valid solns

        # count(n) = {
        #               0 if n < 0,
        #               1 if n == 0,
        #               else count(n - 1) + count(n - 2)
        #            }

        # recursively
        # ready = [False]*(n+1)
        # count_arr = [0]*(n+1)
        # def count(n):
        #     if ready[n]:
        #         return count_arr[n]
        #     if n == 0:
        #         return 1
        #     if n < 0:
        #         return 0
        #     res = count(n-1) + count(n-2)
        #     ready[n] = True
        #     count_arr[n] = res
        #     return res

        # return count(n)

        # iteratively

        ready = [False]*(n+1)
        count = [0]*(n+1)
        count[0] = 1

        for i in range(1, n+1):
            for j in range(1, 3):
                if i - j >= 0:
                    count[i] += count[i-j]
        return count[n]







