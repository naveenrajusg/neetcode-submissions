import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {}
        for i in range(1,n+1):
            adj[i] = []

        for s,d,w in times:
            adj[s].append((d,w))

        shortest = {}

        minheap = [(0,k)]

        while minheap:
            w1, n1  = heapq.heappop(minheap)

            if n1 in shortest:
                continue
            
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 in shortest:
                    continue
                
                heapq.heappush(minheap,(w1+w2, n2))
        

        if len(shortest)==n:
            return max(shortest.values())
        else:
            return -1
    

