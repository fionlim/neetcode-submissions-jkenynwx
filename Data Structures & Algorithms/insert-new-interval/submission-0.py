class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        stop = None
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.append(intervals[i])
                stop = i + 1
                break
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                continue
            else:
                tmp_l = min(newInterval[0], intervals[i][0])
                tmp_r = max(newInterval[1], intervals[i][1])
                newInterval = [tmp_l, tmp_r]
                print("NewInterval:", newInterval)

        if stop:
            for i in range(stop, len(intervals)):
                res.append(intervals[i])
        else:
            res.append(newInterval)
        
        return res

        

            

        
        
            

            
            

