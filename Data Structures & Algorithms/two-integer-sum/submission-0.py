class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = dict()
        for i in range(len(nums)):
            elem = nums[i]
            diff = target - elem
            if diff not in hashset:
                hashset[elem] = i
            else:
                return [hashset[diff], i]