class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        pref = [0 for _ in range(len(nums))]
        pref[0] = nums[0]
        for i in range(1, len(pref)):
            pref[i] = pref[i-1]+ nums[i]
        
        l,r = 0,0
        ans = 0
        k = len(nums) - k
        
        if k==0: ans = pref[-1]
        while r<len(nums):
            if r-l+1==k:
                print('hi')
                if l==0: ans = max(ans, pref[-1] - pref[r])
                else: ans = max(ans, pref[-1] - pref[r] + pref[l-1])
                l+=1
            r+=1
        
        return ans


        
        