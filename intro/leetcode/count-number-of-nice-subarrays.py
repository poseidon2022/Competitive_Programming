class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = []
        for idx, val in enumerate(nums):
            if val%2!=0: odd.append(idx)
        
        odd = odd[::-1]
        count = 0
        l,r = 0,0
        ans = 0
        while r<len(nums):
            if nums[r]%2!=0: count+=1
            while count>k:
                if nums[l]%2!=0:
                    count-=1
                    odd.pop()
                    l+=1
                    break
                l+=1
            if count==k: ans+=(odd[-1] - l + 1)
            r+=1
        
        return ans

            
