import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        # upper bound of k 
        upper_k = math.ceil(sum(piles) / (h - len(piles)))
        print(upper_k)
        k_range = range(1, upper_k + 1)
        start_ptr = 0
        end_ptr = len(k_range) - 1
        res = None
        while start_ptr <= end_ptr:
            mid_ptr = (start_ptr + end_ptr) // 2
            k = k_range[mid_ptr]
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)
            if total_time <= h: # total time less than h so can reduce k
                end_ptr = mid_ptr - 1
                res = k
            else: # total time exceeded h so must increase k
                start_ptr = mid_ptr + 1 
        return res
             
        
