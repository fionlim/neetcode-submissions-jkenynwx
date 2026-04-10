import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, num * -1)

        res = None
        for i in range(k):
            res = heapq.heappop(h)
        return res * -1