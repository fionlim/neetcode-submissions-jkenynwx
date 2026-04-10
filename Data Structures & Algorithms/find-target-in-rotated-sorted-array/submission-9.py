class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1

        while left_ptr <= right_ptr:
            mid_ptr = (left_ptr + right_ptr) // 2
            print('left_ptr: ' + str(left_ptr))
            print('right_ptr: ' + str(right_ptr))
            print('mid_ptr: ' + str(mid_ptr))
            if nums[mid_ptr] == target:
                return mid_ptr
            # left to right ptr sorted
            elif nums[left_ptr] < nums[right_ptr]:
                if nums[mid_ptr] > target:
                    right_ptr = mid_ptr - 1
                else:
                    left_ptr = mid_ptr + 1
            # left side of mid sorted
            elif nums[left_ptr] <= nums[mid_ptr]:
                # check if target is in the range, biggest no. rotated first
                if target >= nums[left_ptr] and target <= nums[mid_ptr]:
                    right_ptr = mid_ptr - 1
                else:
                    left_ptr = mid_ptr + 1
            # right side of mid sorted
            elif nums[mid_ptr] < nums[right_ptr]:
                if target >= nums[mid_ptr] and target <= nums[right_ptr]:
                    left_ptr = left_ptr + 1
                else:
                    right_ptr = mid_ptr - 1

        return -1
                    