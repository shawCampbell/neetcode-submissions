class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # k = [i for i in range(1, kmax+1)]

        l, r = 1, max(piles)

        def compute_t(k):
            t = 0
            for p in piles[::-1]:
                t += math.ceil(p/k)
                if t > h:
                    return False
            return True


        while l < r:
            m = l + (r - l)//2

            t = compute_t(m)

            if t:
                r = m
            else:
                l = m + 1
        
        return l