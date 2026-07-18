import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}

        for i in range(len(points)):
            x,y = points[i]
            adj[(x,y)]=[]

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)

                adj[(x1, y1)].append((dist,(x1,y1),(x2,y2)))
                adj[(x2, y2)].append((dist,(x2,y2),(x1,y1)))

        visited = set()
        mst = []
        minheap = []
        for dist, src, dst in adj[tuple(points[0])]:
            heapq.heappush(minheap,(dist,src,dst))

        visited.add(tuple(points[0]))
        total_dist = 0
        while minheap:
            dist, src, dst = heapq.heappop(minheap)
            if dst in visited:
                continue

            mst.append((src,dst))
            visited.add(dst)
            
            total_dist+= dist

            for weight, src1, dst1 in adj[dst]:
                if dst1 in visited:
                    continue
                heapq.heappush(minheap,(weight, src1, dst1))

        if len(visited)==len(points):
            return total_dist
        else:
            return -1


