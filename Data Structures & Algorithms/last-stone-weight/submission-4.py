class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if b>a:
                heapq.heappush(stones, -(abs(a)-abs(b)))
            elif a==b:
                continue
        
        if len(stones)==0: 
            stones.append(0)
        return(abs(stones[0]))
