class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}

        for i in range(n):
            adj[i] = []

        for s, d, w in edges:
            adj[s].append((d,w))

        shortest = {}
        minheap = [(0,src)]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap,(w1+w2, n2))

        for node in range(n):
            if node not in shortest:
                shortest[node] = -1

        return shortest 