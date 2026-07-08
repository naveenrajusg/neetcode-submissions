class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res #The confusing part is that append() changes the list, but it does not give the list back. That's why if we do return res.append(newInterval) it will return None