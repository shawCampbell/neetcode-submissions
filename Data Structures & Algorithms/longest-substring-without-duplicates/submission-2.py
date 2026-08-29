class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mRes = 0

        p1 = 0
        seen = set()
        
        for p2 in range(len(s)):
            while s[p2] in seen:
                seen.remove(s[p1])
                p1 += 1
            seen.add(s[p2])
            mRes = max(mRes, p2 - p1 + 1)
        return mRes