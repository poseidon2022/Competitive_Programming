class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        i,j = 0,len(nums)-1
        while i<j:
            if nums[i] + nums[j] > k: j-=1
            elif nums[i] + nums[j] < k: i+=1
            else: 
                ans+=1
                i,j = i+1, j-1

        return ans        