class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # dict to map each num to remaining sum
        d = {}

        for i in range(len(nums)):
            n = nums[i]
            if n in d: # continue if num done already 
                continue
            res = []
            target_sum = 0 - n
            temp = set()
            done = set()
            for j in range(len(nums)):
                if i == j:
                    continue
                m = nums[j] # number to match 
                if m in done:
                    continue

                target_val = target_sum - m 

                if target_val in temp and target_val not in d and m not in d: # check that target val and m not covered in outer loop
                    res.append([n, m, target_val])
                    done.add(m)
                else:
                    temp.add(m) # for matching of upcoming nums
            d[n] = res

        output = []
        for item in d.values():
            for sub_item in item:
                output.append(sub_item)
        return output
            
            
                

            