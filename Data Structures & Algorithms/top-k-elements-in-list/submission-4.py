class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        count_reversed = []
        for n, cnt in count.items():
            count_reversed.append([cnt,n])
        count_reversed.sort()

        res = []

        while len(res)<k:
            res.append(count_reversed.pop()[1])
        
        return res

