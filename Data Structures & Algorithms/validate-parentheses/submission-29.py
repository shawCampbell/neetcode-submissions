class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        reverse = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != reverse[c]:
                return False

        return True if len(stack) == 0 else False
            
