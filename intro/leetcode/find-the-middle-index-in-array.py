class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        pref = [0 for _ in range(len(nums))]
        pref[0] = nums[0]
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + nums[i]
        
        for i in range(len(nums)):

            if (i==0 and pref[-1]-nums[i]==0) or (i==len(nums)-1 and pref[i-1]==0)  or (i!=0 and i!=len(nums)-1 and pref[i-1]==pref[-1] - pref[i]):
                return i
            
        return -1

        