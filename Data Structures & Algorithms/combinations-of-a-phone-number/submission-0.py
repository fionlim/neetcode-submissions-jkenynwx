class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        if len(digits) == 0:
            return res

        def dfs(i, cur):
            if i >= len(digits):
                res.append(cur)
                return
            d = int(digits[i])
            for c in letters[d - 2]:
                cur += c
                dfs(i + 1, cur)

                cur = cur[:-1]
        
        dfs(0, "")
        return res
