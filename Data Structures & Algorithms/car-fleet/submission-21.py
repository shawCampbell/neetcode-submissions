class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # s = d/t
        
        p_s = [[p, s, (target-p)/s] for p,s in zip(position, speed)]
        p_s = sorted(p_s, key=lambda x: -x[0])

        stack = []
        res = 0
        for p,s,t in p_s:
            if stack and t <= stack[-1][2]:
                stack.append([p,s,stack[-1][2]])
            else:
                stack = [[p,s,t]]
                res += 1
        return res
