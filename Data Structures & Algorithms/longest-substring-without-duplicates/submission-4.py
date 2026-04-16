class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l, r = 0, 1
        dup = {}
        dup[s[l]] = l
        longest = 0
        while r < len(s):
            if s[r] not in dup or dup[s[r]] < l: # new char or not in curr sequence
                dup[s[r]] = r # update idx of char
                longest = max(longest, r - l + 1)
                r += 1 
            else:
                l = dup[s[r]] + 1
        return longest
