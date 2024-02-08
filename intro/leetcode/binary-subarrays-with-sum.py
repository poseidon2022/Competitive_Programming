class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        mine = defaultdict(int)
        ans = 0
        cur = 0
        mine[0] = 1
        for i in range(len(nums)):
            cur+=nums[i]
            ans+=mine[cur - goal]
            mine[cur]+=1
        
        return ans

