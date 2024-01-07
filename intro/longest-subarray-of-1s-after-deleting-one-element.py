class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i,j = 0,0
        count = 0
        ans = 0
        while j<len(nums):
            if nums[j]==0: count+=1
            if count==2 and nums[j]==0:
                ans = max(ans, j-i-1)
                print(ans, j, i)
                while count==2:
                    if nums[i]==0: count-=1
                    i+=1
            j+=1

        return max(ans, j-i-1)



        