class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        cur = intervals[0]
        res = []
        
        for i in range(1,len(intervals)):
            if cur[1] < intervals[i][0]:
                res.append(cur)
                cur = intervals[i]
            elif cur[0] > intervals[i][1]:
                res.append(intervals)
                continue
            else:
                tmp_l = min(cur[0], intervals[i][0])
                tmp_r = max(cur[1], intervals[i][1])
                cur = [tmp_l, tmp_r]
        res.append(cur)
        return res