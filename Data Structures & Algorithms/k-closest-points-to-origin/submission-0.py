import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            x, y = point
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (distance, point))
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res