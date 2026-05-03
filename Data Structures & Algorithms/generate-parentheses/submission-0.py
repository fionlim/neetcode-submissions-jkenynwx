class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(i, j, cur): 
            # can only add close when there is open
            # i: count of number of open brackets
            # j: count of number of close brackets
            if j == n:
                res.append(cur)
                return 

            # choose to add another open bracket
            if i < n:
                cur += "("
                dfs(i + 1, j, cur)
                cur = cur[:-1]

            # choose to close bracket
            if j < i:
                cur += ")"
                dfs(i, j + 1, cur)

        dfs(0, 0, "")
        return res