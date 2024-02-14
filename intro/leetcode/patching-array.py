class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        ans = 0
        v = 0
        _cur = 0
        if nums[0]==1:
            _cur = 1
            v = 1
        for i in range(v, len(nums)):
            
            if _cur >= n: return ans
            while _cur + 1 < nums[i]:
                ans+=1
                _cur+=_cur+1
                if _cur >= n: return ans

            _cur+=nums[i]
        
        while _cur < n:
            ans+=1
            _cur+=_cur+1
        
        return ans 




        