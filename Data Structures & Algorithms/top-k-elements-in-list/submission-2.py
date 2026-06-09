class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = dict()
        for num in nums: 
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        bucket = [[],] * len(nums)

        for num, c in counts.items():
            temp = bucket[c - 1].copy()
            bucket[c - 1] = temp + [num,]

        hashset = set()
        pointer = len(nums) - 1 # start from back 
        while len(hashset) < k:
            hashset.update(bucket[pointer])
            pointer -= 1
        return list(hashset)


