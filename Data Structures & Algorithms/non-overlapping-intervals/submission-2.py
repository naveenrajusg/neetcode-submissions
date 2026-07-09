class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])

        tracked = intervals[0]
        count = 0
        for start, end in intervals[1:]:

            if start<tracked[1]:
                tracked[1] = min(tracked[1],end)
                count+=1
            else:
                tracked = [start,end]

        return count