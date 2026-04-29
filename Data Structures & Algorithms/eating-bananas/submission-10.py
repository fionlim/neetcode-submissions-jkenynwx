import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2 # eating rate per hour
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            print("total:", total)
            print("k:", k)
            if total <= h: # have extra time, decrease k
                r = k - 1
            else: # exceed time, increase k
                l = k + 1

        return l
                
        
