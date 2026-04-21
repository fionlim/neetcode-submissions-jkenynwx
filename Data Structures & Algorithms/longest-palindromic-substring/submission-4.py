class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        res_len = 0
        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i # centre

            while l >= 0 and r < len(s) and s[l] == s[r]: # check if is an odd palindrome
                if len(s[l:r+1]) > res_len:
                    res = s[l:r+1]
                    res_len = len(res)
                l -= 1
                r += 1
            
            # even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > res_len:
                    res = s[l:r+1]
                    res_len = len(res)
                l -= 1
                r += 1

        return res
