class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0,] * len(temperatures)

        s = [] # stack to keep track of min temp

        for i in range(len(temperatures)):
            t = temperatures[i]
            while s and s[-1][1] < t:
                prev = s.pop(-1)
                res[prev[0]] = i - prev[0]
            s.append((i, t))
            print(s)

        return res



