class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        s = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        while s:
            pos, speed = s.pop(0)
            res += 1
            while s and (target - s[0][0]) / s[0][1] <= (target - pos) / speed:
                s.pop(0)

        return res
            

