class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        res = True
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                print("left:",s[l])
                print("right:",s[r])
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                    continue
                else:
                    res = False
                    break
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1
        return res
