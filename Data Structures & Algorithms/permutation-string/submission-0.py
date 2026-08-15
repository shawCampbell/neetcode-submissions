class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        f1 = [0 for i in range(26)]

        for c in s1:
            f1[ord(c) - ord('a')] += 1

        l = 0
        f2 = [0] * 26
        maxS = 0
        for r in range(len(s2)):
            f2[ord(s2[r]) - ord('a')] += 1

            f_1 = f1[ord(s2[r]) - ord('a')]
            f_2 = f2[ord(s2[r]) - ord('a')]

            while f_2 > f_1:
                f2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                f_2 = f2[ord(s2[r]) - ord('a')]

            maxS = max(maxS, r - l + 1) 
            print(s2[l:r+1])

        return True if maxS == len(s1) else False

