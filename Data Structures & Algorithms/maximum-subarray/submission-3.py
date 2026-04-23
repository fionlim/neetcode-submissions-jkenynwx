class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = res = nums[0]
        for n in nums[1:]:
            tmp = res + n
            print(tmp)
            if tmp < 0:
                if res >= 0:
                    res = 0
                else:
                    res = max(res, n)
            else:
                res = tmp
            maxSum = max(maxSum, res)
        return maxSum