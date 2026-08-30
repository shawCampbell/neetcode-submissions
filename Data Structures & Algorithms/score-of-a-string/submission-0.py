class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        c = s[0]
        for i in range(1, len(s)):
            res += abs(ord(s[i]) - ord(c))
            c = s[i]

        return res