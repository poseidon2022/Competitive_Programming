class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j = 0,0
        ans = 0
        while j<len(nums):
            if k==0 and nums[j]==0:
                ans = max(ans,j-i)
                while k==0:
                    if nums[i]==0: k+=1
                    i+=1
            if nums[j]==0: k-=1
            j+=1
        
        print(i,j)
        return max(ans,j-i)
        