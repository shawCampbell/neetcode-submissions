class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        square_map = {(x**2+y**2): [] for x,y in points}
        for x,y in points:
            square_map[(x**2+y**2)].append([x, y])
        print(square_map)

        squares = list(square_map.keys())
        heapq.heapify(squares)

        res = []
        while len(res) != k:
            square = heapq.heappop(squares)
            res.extend(square_map[square])

        return res
        