class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        m = {
            '+': lambda x,y: x+y,
            '*': lambda x,y: x*y,
            '-': lambda x,y: x-y,
            '/': lambda x,y: int(x/y)
        }
        st = []
        for s in tokens:
            if s not in m:
                st.append(int(s))
            else:
                y = st.pop()
                x = st.pop()
                if y == 17:
                    print(s, x)
                st.append(m[s](x, y))
        return st[0]