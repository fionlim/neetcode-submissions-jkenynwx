class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        mem = {}
        if amount == 0:
            return 0

        def dp(amount):
            if amount < 0:
                return -1
            if amount in mem:
                return mem[amount]
            if amount in coins:
                mem[amount] = 1
                return 1
            else:
                temp = 10e99
                possible = False
                for n in coins:
                    sub_dp = dp(amount - n)
                    if sub_dp != -1:
                        possible = True
                        temp = min(temp, sub_dp + 1)
                if possible:
                    mem[amount] = temp
                else:
                    mem[amount] = -1
                return mem[amount]

        return dp(amount)
                



