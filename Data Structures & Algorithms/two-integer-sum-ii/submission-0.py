class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binary_search(arr, k):
            if k < arr[0] or k > arr[-1]:
                return 
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if k == arr[m]:
                    return m
                if k < arr[m]:
                    r = m - 1
                else:
                    l = m + 1
            return 

        res = []
        for i in range(len(numbers) - 1):
            ind = binary_search(numbers[i + 1:], target - numbers[i])
            if ind is not None:
                res = [i + 1, i + ind + 2]
                break
        
        return res
