# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2: return 0
        ans = sorted(nums)
        _ans = float('-inf')
        for i in range(1,len(ans)):
            if ans[i]-ans[i-1]>_ans: _ans = ans[i]-ans[i-1]
        
        return _ans
        
        