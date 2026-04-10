class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_arr = [False,] * len(nums)
        zero_counter = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_counter += 1
                zero_arr[i] = True
                continue
            product = product * nums[i]

        arr = [0,] * len(nums)
        if zero_counter > 1:
            return arr

        for i in range(len(nums)):
            if nums[i] != 0 and zero_counter == 0:
                arr[i] = product // nums[i]
            elif nums[i] == 0:
                arr[i] = product

        return arr

