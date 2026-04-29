class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        res = ""
        max_heap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))

        while max_heap:
            count, char = heapq.heappop(max_heap)
            if count == 0: # max freq is 0, no more chars left
                break
            if len(res) > 1 and res[-1] == res[-2] == char:
                count1, char1 = heapq.heappop(max_heap)
                if count1 == 0:
                    break
                else:
                    res += char1
                    count1 += 1 
                    heapq.heappush(max_heap, (count1, char1))
            else:
                res += char
                count += 1
            heapq.heappush(max_heap, (count, char))
        return res





        
