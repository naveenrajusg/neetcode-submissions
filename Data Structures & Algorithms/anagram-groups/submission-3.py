from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str_val in strs:
            count = [0]*26
            for s in str_val:
                count[ord(s)-ord('a')]+=1
            result[tuple(count)].append(str_val)
        return list(result.values())