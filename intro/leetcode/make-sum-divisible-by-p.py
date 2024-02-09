class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        tar = sum(nums)%p
        if tar==0: return 0
        ans = float('inf')
        mine = defaultdict(int)
        mine[0] = -1
        cur = 0
        for i in range(len(nums)):
            cur+=nums[i]
            if (cur%p - tar)%p in mine: ans = min(ans, i - mine[(cur%p - tar)%p])
            mine[cur%p] = i
        
        return -1 if ans==len(nums) else ans 

              