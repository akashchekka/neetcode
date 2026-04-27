class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, [x, y]))

        for _ in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)

        return res