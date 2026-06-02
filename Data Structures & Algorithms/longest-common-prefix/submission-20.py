class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for i in range(len(strs[0])):
            
            for s in strs[1:]:
                if len(s)==0:
                    return ""
                elif i>=len(s):
                    result = strs[0][:i]
                    return result
                elif s[i]!=strs[0][i]:
                    return strs[0][:i]
                result = strs[0][:i+1]

        return result


