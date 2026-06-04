import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Find shortest path from k to all n nodes
        path = {}

        # detect cycle
        visit = set() 

        # transform to edge list
        edges = {}
        for i in range(1, n + 1):
            edges[i] = []

        for u, v, w in times:
            edges[u].append((w, v)) # priority val must be first element

        # use priority queue
        pq = []
        heapq.heappush(pq, (0, k))
        path[0] = 0

        while pq:
            w, v = heapq.heappop(pq)

            if v in visit:
                continue

            visit.add(v)

            path[v] = w

            for wi, vi in edges[v]:
                heapq.heappush(pq, (wi + w, vi))

        if len(path) < n + 1:
            return -1

        return max(path.values())
        
            

        
            

