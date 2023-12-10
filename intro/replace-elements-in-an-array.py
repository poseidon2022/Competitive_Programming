class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mine = defaultdict(int)
        for idx, val in enumerate(nums):
            mine[val] = idx
        
        for replaced, replacer in operations:
            nums[mine[replaced]] = replacer
            mine[replacer] = mine[replaced]
            del mine[replaced]
        
        return nums
        