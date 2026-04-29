class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d = {}
        for char in s1:
            if char not in d:
                d[char] = 0
            d[char] += 1

        def is_anagram(s2, d):
            for char in s2:
                if char not in d:
                    return False
                d[char] -= 1
            
            for _, count in d.items():
                if count != 0:
                    return False
            return True

        l, r = 0, len(s1) - 1
        tmp = d.copy()
        while r < len(s2):
            if is_anagram(s2[l: r + 1], d):
                return True
            l += 1
            r = l + len(s1) - 1
            d = tmp.copy()
        return False
        



