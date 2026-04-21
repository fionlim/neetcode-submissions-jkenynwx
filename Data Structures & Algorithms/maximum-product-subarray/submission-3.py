class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = 0
        minCur = nums[0]
        maxCur = nums[0]
        if len(nums) <= 1:
            return nums[0]
            
        for n in nums[1:]:
            if n > 0:
                maxCur = max(n, maxCur * n)
                minCur = min(n, minCur * n)
            elif n < 0:
                temp = minCur
                minCur = min(n, n * maxCur)
                maxCur = max(n, temp * n)
            else: # n == 0
                minCur, maxCur = 1, 1
                continue
            print("min:", minCur)
            print("max:", maxCur)
            print("maxProd:", maxProd)
        
            maxProd = max(maxCur, maxProd)
        
        return maxProd