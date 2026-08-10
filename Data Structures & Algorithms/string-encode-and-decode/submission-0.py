class Solution:

    def encode(self, strs: List[str]) -> str:
        for i, s in enumerate(strs):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        res = []
        
        while len(s) > 0:
            meta = s[:s.index('#')]
            l = int(meta)
            res.append(s[s.index('#') + 1: s.index('#') + 1 + l])
            s = s[s.index('#') + l + 1:]
            # print(meta, s, res, sep = ' - ')

        return res




















    #     latents = []

    #     for s in strs:
    #         latent = [0 for i in range(256)]
    #         for c in s:
    #             latent[ord(c)]+=1
    #         latents.append(latent)

    #     return latents



    # def decode(self, s: str) -> List[str]:
        
    #     for i in range(256):
    #         if ()
        
