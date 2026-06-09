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
        if key not in self.timemap:
            return ""
        arr = self.timemap[key]
        l, r = 0, len(arr) - 1
        mid, t = -1, -1
        while l <= r:
            mid = (l + r) // 2
            value, t = arr[mid]
            if t == timestamp:
                return value
            if t > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        if arr[mid][1] < timestamp:
            return arr[mid][0]
        elif arr[mid - 1][1] < timestamp:
            return arr[mid - 1][0]

        return ""

