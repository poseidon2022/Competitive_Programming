class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        _min = 0
        pref = [0 for _ in range(len(nums))]
        pref[0]  = nums[0]
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + nums[i]
        
        ans = float('-inf')
        for i in range(len(pref)):
            ans = max(ans, pref[i] - _min)
            _min  = min(_min, pref[i])
        
        return ans

        



        