class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlength = 0 
        l=0
        r=0
        count={}

        while (r<len(s)):
            count[s[r]] = 1+count.get(s[r],0)

            cur_values = count.values()
            if (r-l+1) - max(cur_values)<=k:
                maxlength = max(maxlength,r-l+1)
                r+=1
            else:
                count[s[l]]-=1
                l=l+1
                r=r+1
        return maxlength            






