class Solution:
    def numDecodings(self, s: str) -> int:

        dp = dp2 = 0
        dp1 = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1                
                if 10 <= int(s[i:i+2]) <= 26:
                    dp += dp2
                
            dp2 = dp1
            dp1 = dp

        return dp1
