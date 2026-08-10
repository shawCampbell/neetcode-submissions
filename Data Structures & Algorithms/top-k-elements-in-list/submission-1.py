class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {num: 0 for num in nums}

        for num in nums:
            map[num] += 1

        sort_freq = sorted(map.keys(), key= lambda x: map[x])

        print(sort_freq)

        res = sort_freq[len(sort_freq)-k: len(sort_freq)]

        return res
