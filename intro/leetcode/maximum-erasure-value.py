class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        mine = defaultdict(int)
        _sum = 0
        ans = float('-inf')
        while r<n:
            mine[nums[r]]+=1
            while len(mine) < r-l+1:
                print(l,r)
                mine[nums[l]]-=1
                _sum-=nums[l]
                if not mine[nums[l]]: del mine[nums[l]]
                l+=1

            _sum+=nums[r]
            ans = max(ans, _sum)
            r+=1
        
        return ans

        