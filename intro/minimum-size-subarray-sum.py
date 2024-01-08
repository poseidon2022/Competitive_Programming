class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _min = float('inf')
        l, r = 0, 0
        r_sum = 0
        while r<len(nums):
            r_sum+=nums[r]
            while r_sum>=target:
                _min = min(_min, r-l+1)
                r_sum-=nums[l]
                l+=1
            r+=1


        return 0 if _min==float('inf') else _min
        