class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        m = [[] for i in range(26)]
        for i,c in enumerate(s):
            m[ord(c) - ord('a')].append(i)
        maxR = -1
        print(m)
        for x in m:
            if len(x) == 0:
                continue
            for y in x:
                for z in x:
                    maxR = max(maxR, abs(y-z)-1)
        return maxR