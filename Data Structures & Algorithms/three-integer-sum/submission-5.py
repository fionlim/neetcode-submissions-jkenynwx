class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        done = set()
        for i in range(len(nums)):
            if nums[i] in done:
                continue
            target = 0 - nums[i]
            d = set()
            done2 = set()
            for j in range(i + 1, len(nums)): # only check ahead to avoid duplicates
                if nums[j] in done or nums[j] in done2:
                    continue
                match = target - nums[j]
                if match in d:
                    res.append([nums[i], nums[j], match])
                    done2.update([nums[j], match])
                else:
                    d.add(nums[j])
            done.add(nums[i])
        return res