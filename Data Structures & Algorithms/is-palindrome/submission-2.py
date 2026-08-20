class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            if not self.an(s[l]) or not self.an(s[r]):
                while l < len(s) and not self.an(s[l]):
                    l += 1
                while r >= 0 and not self.an(s[r]):
                    r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True

    def an(self, ch):
        c = ord(ch)
        return (ord('a')<=c<=ord('z') or
                ord('A')<=c<=ord('Z') or
                ord('0')<=c<=ord('9'))