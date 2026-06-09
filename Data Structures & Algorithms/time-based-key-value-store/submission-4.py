class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp]) 
        # value, timestamps added in strictly increasing order, so list is sorted

    def get(self, key: str, timestamp: int) -> str:
        # binary search to improve efficiency of finding value using timestamp
        res = ""

        arr = self.timemap.get(key, [])
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            value, mid_t = arr[mid]
            if mid_t <= timestamp:
                res = value
                l = mid + 1
            else:
                r = mid - 1
                
        return res

