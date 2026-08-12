class TimeMap:

    # (x1, v1, t0), (x2, v2, t2), (x3, v3, t3), ... , (x4, v4, t4)
    # set(xn, vn, tn) -> map.put(V) or update (xk, vk, tk) with new val ect.
    # get(xk, tp) -> (xk, vk, tk) last V that had an existing tk
    # L= L= L= L= L= B B B B

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if value != "":
            self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        li = self.m[key]
        if not (li):
            return ""
        l, r = 0, len(li) - 1
        mi = 0
        #print("call:", self.m, li, sep=", ")

        while l < r:
            mi = l + math.ceil((r - l)/2)

            if timestamp >= li[mi][0]:
                l = mi
            else:
                r = mi - 1
        #print("Must return l[", l,",][", 1, "]", ", with li being: ", li, sep="")
        return li[l][1] if li[l][0] <= timestamp else ""

        

