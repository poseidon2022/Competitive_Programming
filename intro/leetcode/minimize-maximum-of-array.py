class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cur = 0
        ans = float('-inf')
        for i in range(len(nums)):
            cur += nums[i]
            ans = max(ans, math.ceil(cur / (i + 1)))
        
        return ans
            
        