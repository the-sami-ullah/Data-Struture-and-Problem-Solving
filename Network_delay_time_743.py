import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i: [] for i in range(1, n + 1)}
        for src, des, w in times:
            adj[src].append((des, w))

        
        minHeap = [(0, k)]
        shortest = {}

        
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in shortest:
                continue  
            shortest[node] = time

            for nei, wt in adj[node]:
                if nei not in shortest:
                    heapq.heappush(minHeap, (time + wt, nei))

        
        if len(shortest) != n:
            return -1
        print(shortest)
        print(adj)
        # Return the longest shortest path
        return max(shortest.values())
