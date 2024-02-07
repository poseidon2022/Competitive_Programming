class Solution:
    def maxScore(self, s: str) -> int:
        nums = list(map(int, s))
        pref = [0 for _ in range(len(nums))]
        pref[0] = nums[0]
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + nums[i]
        
        ans = 0
        for i in range(len(nums)-1):
            ans = max(ans, i - 2*pref[i] + 1 + pref[-1])
        
        return ans
        
        
        
        