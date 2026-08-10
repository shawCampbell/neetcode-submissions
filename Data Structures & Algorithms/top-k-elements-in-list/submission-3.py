class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = [[] for num in nums]
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for n, f in freq.items():
            freq_map[f-1].append(n)

        res = []
        i = len(freq_map) - 1
        while True:
            if len(freq_map[i]) > 0:
                res.append(freq_map[i].pop())
                if len(res) == k:
                    return res
            else:
                i -= 1










        # map = {num: 0 for num in nums}

        # for num in nums:
        #     map[num] += 1

        # sort_freq = sorted(map.keys(), key= lambda x: map[x])

        # res = sort_freq[len(sort_freq)-k: len(sort_freq)]

        # return res
