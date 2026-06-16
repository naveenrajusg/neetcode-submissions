class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        counter=1
        stack=[]
        for i in range(0,len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                prev = stack.pop()
                res[prev]=i-prev
            stack.append(i)
        return res