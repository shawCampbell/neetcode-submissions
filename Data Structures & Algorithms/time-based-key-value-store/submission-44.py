class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.m:
            self.m[key].append([value, timestamp])
        else:
            self.m[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.m:
            return ""
        l, r = 0, len(self.m[key]) - 1
        while l < r:
            mid = l + math.ceil((r - l)/2)

            if self.m[key][mid][1] <= timestamp:
                l = mid 
            else:
                r = mid - 1
        # if self.m[key][l][0] == "":
        #     print(key, timestamp)
        return self.m[key][l][0] if self.m[key][l][1] <= timestamp else ""


        
