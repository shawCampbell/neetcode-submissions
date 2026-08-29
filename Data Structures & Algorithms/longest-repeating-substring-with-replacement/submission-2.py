class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        m = {c: 0 for c in s}
        max_res = 0
        
        l = 0
        for r in range(len(s)):
            m[s[r]] += 1

            while max(m.values()) < r-l+1 - k:
                m[s[l]] -= 1
                l += 1
    
            max_res = max(max_res, r-l+1)
        return max_res

