class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for elem in nums:
            if elem in hashmap:
                return True
            else:
                hashmap.add(elem)
        return False