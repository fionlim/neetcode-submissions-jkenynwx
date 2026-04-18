class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = -1
        maxf = 0 # freq of highest occurring char
        d = {} # track freq of chars in window
        longest = 0 

        for l in range(len(s)): 

            while (r - l + 1) - maxf <= k and r < len(s) - 1: # have leeway for replacements or num replacements hit but can still continue
                r += 1 # grow window on right
                if s[r] not in d: # new char 
                    d[s[r]] = 0
                d[s[r]] += 1 # add char freq to window
                maxf = max(d[s[r]], maxf)
                if (r - l + 1) - maxf <= k:
                    longest = max(longest, r - l + 1)

            d[s[l]] -= 1 # remove left char from window and decrease its freq

        return longest
        


            
            
                