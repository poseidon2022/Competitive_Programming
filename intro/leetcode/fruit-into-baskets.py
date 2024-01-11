class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        mine  = defaultdict(int)
        l,r = 0,0
        ans = float('-inf')
        while r<len(nums):
            mine[nums[r]]+=1
            while len(mine)>2:
                mine[nums[l]]-=1
                if not mine[nums[l]]: del mine[nums[l]]
                l+=1
            ans = max(ans, r-l+1)
            r+=1
        
        return ans
