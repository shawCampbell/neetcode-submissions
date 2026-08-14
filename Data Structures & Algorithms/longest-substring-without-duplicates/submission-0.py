class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        maxS = 1
        seen = set()

        seen.add(s[l])
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxS = max( maxS, r - l + 1)
            r += 1

        return maxS
                
            
            