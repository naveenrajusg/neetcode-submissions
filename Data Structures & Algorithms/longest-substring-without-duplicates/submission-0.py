class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l=0
        r=0
        longest = 0

        while r<len(s):

            while s[r] in window:
                window.remove(s[l])
                l=l+1

            if s[r] not in window:
                window.add(s[r])
        
            longest = max(longest,r-l+1)
            r+=1
        return longest