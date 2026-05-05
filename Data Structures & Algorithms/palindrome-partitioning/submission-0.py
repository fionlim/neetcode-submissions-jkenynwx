class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(l, r, cur):
            if l >= len(s):
                res.append(cur.copy())
                return
            if r >= len(s):
                return
            if is_palindrome(s[l:r+1]):
                cur.append(s[l:r+1])

                dfs(r + 1, r + 1, cur)
                cur.pop()

            # expand window on right side
            dfs(l, r + 1, cur)

        dfs(0, 0, [])
        return res
