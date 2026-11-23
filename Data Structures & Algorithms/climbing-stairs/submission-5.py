class Solution:
    def climbStairs(self, n: int) -> int:
        # steps = n
        # k = {1, 2}
        # x(n) = {
        #   1 if n == 1
        #   2 if n == 2
        #   else x(n-1) + x(n-2)
        #{

        one, two = 1, 2

        if n == 1:
            return one
        if n == 2:
            return two

        for i in range(n - 2):
            temp = two
            two = one + two
            one = temp

        return two