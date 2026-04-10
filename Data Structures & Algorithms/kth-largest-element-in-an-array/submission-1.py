import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap method
        # h = []
        # for num in nums:
        #     heapq.heappush(h, num * -1)

        # res = None
        # for i in range(k):
        #     res = heapq.heappop(h)
        # return res * -1
        
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            p = l # pointer
            for i in range(l, r): # stop before pivot ind
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if k < p:
                return quickSelect(l, p - 1)
            elif k > p:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)
