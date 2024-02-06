class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = [0 for _ in range(len(nums))]
        suff = [0 for _ in range(len(nums))]
        pref[0] = nums[0]
        for i in range(len(pref)):
            pref[i] = pref[i-1] + nums[i]
        
        suff[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] + nums[i]
        
        ans = []
        for i in range(len(nums)):
            p_d = 0 if i==0 else i * nums[i] - pref[i-1]
            s_d = 0 if i==len(nums)-1 else (len(nums) - i - 1)*nums[i] - suff[i+1]
            ans.append(abs(p_d) + abs(s_d))
        
        return ans
    
        