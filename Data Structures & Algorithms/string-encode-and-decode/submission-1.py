class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "#" + s for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            l = 0
            while s[l] != "#":
                l += 1 
            start = l+1
            l = int(s[0: l])
            end = start + l
            res.append(s[start:end])
            print(s[start:end])
            s = s[end:]
        return res
