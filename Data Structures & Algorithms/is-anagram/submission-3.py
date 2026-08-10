class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freq = [0 for i in range(26)]

        for c1, c2 in zip(s, t):
            freq[ord(c1) - ord('a')] += 1
            freq[ord(c2) - ord('a')] -= 1

        return True if all(n == 0 for n in freq) else False