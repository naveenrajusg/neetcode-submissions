class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curset = []
        subset = []

        self.helper(1, n, k, curset, subset)
        return subset
    
    def helper(self,i, n, k, curset, subset):

        if len(curset)==k:         
            subset.append(curset.copy())
            return
        if i>n:
            return

        curset.append(i)
        self.helper(i+1, n, k, curset, subset)

        curset.pop()
        self.helper(i+1, n, k, curset, subset)
