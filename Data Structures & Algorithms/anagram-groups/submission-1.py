class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}

        for s in strs:
            freq = [0 for i in range(26)]
            for c in s:
                freq[ord(c) - ord("a")] += 1
            freq = tuple(freq)
            if freq in map:
                map[freq].append(s)
            else:
                map[freq] = [s]

        return list(map.values())