class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = [0 for _ in range(len(nums))]
        pref[0] = nums[0]
        mine = defaultdict(int)
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + nums[i]
        mine[0] = 1
        ans = 0
        for i in pref:
            tar  = i - k
            if tar in mine: ans+=mine[i-k]
            mine[i]+=1
        
        return ans
        
        
        
        
        

        