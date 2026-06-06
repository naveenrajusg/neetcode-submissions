import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res1=[1]*(len(nums))

        prefix = 1
        for i in range(len(nums)):
            res1[i] = prefix
            prefix = prefix*nums[i]

        postfix=1
        res2=[1]*(len(nums))
        for i in range(len(nums)-1,-1,-1):
            res2[i]= postfix
            postfix = postfix*nums[i]

        res1=np.array(res1)
        res2=np.array(res2)

        res = res1*res2
        return list(res)

        


