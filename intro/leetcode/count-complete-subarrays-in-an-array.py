class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        mine = set(nums)
        l,r = 0,0
        anot = defaultdict(int)
        ans = 0
        while r<len(nums):
            anot[nums[r]]+=1
            while len(anot)==len(mine):
                ans+=len(nums)-r
                anot[nums[l]]-=1
                if not anot[nums[l]]: del anot[nums[l]]
                l+=1
            r+=1
        
        return ans


        