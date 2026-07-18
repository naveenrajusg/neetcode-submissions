import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for i in range(n):
            adj[i] = []

        for s, d, w in edges:
            adj[s].append((d,w))
            adj[d].append((s,w))

        visited = set() 

        minheap = []
        for d, w in adj[0]:
            heapq.heappush(minheap,(w,0,d))

        visited = set()
        visited.add(0)

        mst = []
        total_mst_weight = 0
        while minheap:
            w,s,d = heapq.heappop(minheap)
            if d in visited:
                continue
            mst.append([s,d])
            total_mst_weight+=w
            visited.add(d)

            for neighbour, weight in adj[d]:
                if neighbour in visited:
                    continue
                heapq.heappush(minheap,(weight, d, neighbour))
        
        if len(visited)==n:
            return total_mst_weight
        return -1 

        
       