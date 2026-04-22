class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False,] * (len(s) + 1)
        dp[len(s)] = True # base case: out of bounds

        for i in range(len(s) - 1, -1, -1): # start from end of s
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    print("word:", w)
                    print("i:", i)
                    print("next idx:", i + len(w))
                    print("next idx res:", dp[i + len(w)])
                    if dp[i + len(w)]:
                        dp[i] = dp[i + len(w)]

        return dp[0]


        

                



        
          


        