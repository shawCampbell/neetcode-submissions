class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        f = [set() for i in range(len(nums))]

        m = defaultdict(int)

        res = set()

        for n in nums:
            m[n] += 1
            f[m[n]-1].add(n)

        for l in f[::-1]:
            for j in range(len(l)):
                res.add(l.pop())
                if len(res) == k:
                    return list(res)
            


















        # count = defaultdict(int)

        # for n in nums:
        #     count[n] += 1;

        # heap = []
        # for n, c in count.items():
        #     heapq.heappush(heap, (c, n))
        #     if len(heap) > k:
        #         heapq.heappop(heap) 
        
        # return [n for c, n in heap]

        # freq_map = [[] for num in nums]
        # freq = defaultdict(int)

        # for num in nums:
        #     freq[num] += 1

        # for n, f in freq.items():
        #     freq_map[f-1].append(n)

        # res = []
        # i = len(freq_map) - 1
        # while True:
        #     if len(freq_map[i]) > 0:
        #         res.append(freq_map[i].pop())
        #         if len(res) == k:
        #             return res
        #     else:
        #         i -= 1










        # map = {num: 0 for num in nums}

        # for num in nums:
        #     map[num] += 1

        # sort_freq = sorted(map.keys(), key= lambda x: map[x])

        # res = sort_freq[len(sort_freq)-k: len(sort_freq)]

        # return res
