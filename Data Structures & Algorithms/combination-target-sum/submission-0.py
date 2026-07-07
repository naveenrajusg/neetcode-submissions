class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curset = []

        def helper(i, curset, total):

            if total==target:
                res.append(curset.copy())
                return
            
            if i >=len(nums) or total>target:
                return 

            curset.append(nums[i])
            helper(i,curset, total+nums[i])

            curset.pop()
            helper(i+1, curset, total)


        
        helper(0,curset,0)
        return res