class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings=[]
        for i, num in enumerate(nums):
            mappings.append([num,i])

        mappings.sort()

        i=0
        j=len(nums)-1

        while i<j:
            res = mappings[i][0]+mappings[j][0]
            if res==target:
                return [min(mappings[i][1],mappings[j][1]),max(mappings[i][1],mappings[j][1])]
            elif res<target:
                i+=1
            else:
                j-=1
        return []





