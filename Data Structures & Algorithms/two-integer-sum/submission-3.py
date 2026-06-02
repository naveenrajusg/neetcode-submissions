class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping=[]
        for i,n in enumerate(nums):
            mapping.append([n,i])

        mapping.sort()
        i=0
        j=len(mapping)-1
        while i<j:
            sum = mapping[i][0]+mapping[j][0]
            if sum==target:
                return [min(mapping[i][1],mapping[j][1]),max(mapping[i][1],mapping[j][1])]
            elif sum<target:
                i+=1
            else:
                j-=1
        return []
