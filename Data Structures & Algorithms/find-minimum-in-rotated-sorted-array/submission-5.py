class Solution:
    def findMin(self, nums: List[int]) -> int:
        start_ptr = 0
        end_ptr = len(nums) - 1
        if nums[start_ptr] <= nums[end_ptr]:
            return nums[start_ptr]

        res = None
        while start_ptr <= end_ptr:
            print('start: ' + str(start_ptr))
            print('end: ' + str(end_ptr))
            mid_ptr = (start_ptr + end_ptr) // 2
            # found max
            if nums[mid_ptr] > nums[mid_ptr - 1] and nums[mid_ptr] > nums[mid_ptr + 1]:
                res = nums[mid_ptr + 1]
                break
            # found min
            elif nums[mid_ptr] < nums[mid_ptr - 1] and nums[mid_ptr] > nums[mid_ptr + 1]:
                res = nums[mid_ptr]
                break
            
            # min value somewhere between start and mid pointer
            elif nums[mid_ptr] < nums[start_ptr]:
                res = nums[mid_ptr]
                end_ptr = mid_ptr - 1
            # min value somewhere between mid and end pointer
            else: # middle value > end value, opposite of previous condition
                if res is None or nums[mid_ptr] < res:
                    res = nums[mid_ptr]
                start_ptr = mid_ptr + 1
            print('result: ' + str(res))
        return res