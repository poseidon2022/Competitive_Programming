class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i,j = 0,0
        ans = 0
        while j<len(nums):
            if nums[j]!=1:
                ans = max(ans,j-i)
                j+=1
                i = j
                continue
            j+=1
        ans = max(ans,j-i)
        return ans
        