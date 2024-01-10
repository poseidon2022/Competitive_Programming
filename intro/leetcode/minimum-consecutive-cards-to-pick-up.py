class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        ans = float('inf')
        mine = defaultdict(lambda:-1)
        i,j = 0,0
        while j<len(nums):
            if mine[nums[j]]!=-1:
                ans = min(j-mine[nums[j]]+1,ans)
                mine[nums[j]] = j
                j+=1
                i = j               
                continue
            
            mine[nums[j]] = j
            j+=1
            
        return -1 if ans==float('inf') else ans