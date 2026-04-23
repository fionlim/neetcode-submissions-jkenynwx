class Solution:
    def canJump(self, nums: List[int]) -> bool:
        LENGTH = len(nums)
        d = {}
        print("LENGTH:", LENGTH)
        def dfs(cur):
            print("cur:", cur)
            if cur >= LENGTH - 1:
                return True

            if nums[cur] == 0:
                d[cur] = False
                return False

            for i in range(nums[cur], 0, -1):
                if cur in d:
                    return d[cur]
                if dfs(cur + i):
                    d[cur] = True
                    return True
            d[cur] = False
            return False

        return dfs(0)