class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1 for _ in range(len(nums))]
        pref[0] = nums[0]
        for i in range(1,len(nums)):
            pref[i] = pref[i-1] * nums[i]
        
        suff = [1 for _ in range(len(nums))]
        suff[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] * nums[i]
        
        ans = []
        for i in range(len(nums)):
            if i==0: tar = suff[i+1]
            elif i==len(nums)-1: tar = pref[i-1]
            else: tar = suff[i+1] * pref[i-1]
            ans.append(tar)
        
        return ans
        
        print(suff, pref)

