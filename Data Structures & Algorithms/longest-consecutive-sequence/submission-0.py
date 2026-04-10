class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))

        # each num mapped to its parent
        nums_dict = {num: num - 1 for num in nums}
        print(nums_dict)
        # to skip over numbers that have been handled
        nums_handled = {num: False for num in nums}

        longest = 0

        def find_rep(c):
            p = nums_dict[c]
            if p not in nums_dict: # found a root
                return c
            elif p != c: # not a root
                print(p)
                return find_rep(p) 
            else: # is a root
                return c

        for c in nums_dict:
            nums_dict[c] = find_rep(c)
            diff = c - nums_dict[c] + 1
            if diff > longest:
                longest = diff

        return longest
            
        








        



        








