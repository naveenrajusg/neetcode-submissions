class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in hash_map:
                return [min(i,hash_map[diff]),max(i,hash_map[diff])]
            hash_map[n] = i
        return []