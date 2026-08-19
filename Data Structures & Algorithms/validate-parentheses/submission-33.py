class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 != 0:
            return False 

        st = []

        m = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        i = 0
        while i < len(s):
            if s[i] in m:
                st.append(s[i])

            if s[i] not in m:
                if st and m[st[-1]] == s[i]:
                    st.pop()
                else:
                    return False
            i += 1

        return not st
            