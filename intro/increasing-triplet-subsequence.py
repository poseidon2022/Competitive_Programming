class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        pref_min = [0 for _ in range(len(nums))]
        anot = nums.copy()[::-1]
        pref_min[0] = float('inf')
        for i in range(1, len(nums)):
            pref_min[i] = min(nums[i-1], pref_min[i-1])

        suf_max = [0 for _ in range(len(nums))] 
        suf_max[0] = float('-inf')
        for i in range(1, len(anot)):
            suf_max[i] = max(suf_max[i-1], anot[i-1])
        
        suf_max = suf_max[::-1]
        for i in range(len(nums)):
            if pref_min[i]<nums[i]<suf_max[i]: return True
        
        return False
           
