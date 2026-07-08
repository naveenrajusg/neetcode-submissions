class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curset = []
        res = []

        def helper(i,curset, total):
            if total == target:
                res.append(curset.copy())
                return

            if i>=len(candidates) or total>target:
                return 
            

            curset.append(candidates[i])
            helper(i+1,curset, total+candidates[i])

            curset.pop()
            
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            
            helper(i+1,curset, total)

        helper(0,curset,0)
        return res
