class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        _sum = 0
        for i in nums:
            if i%2==0: _sum+=i

        ans = []
        for val, idx in queries:
            init = nums[idx]
            nums[idx]+=val
            if nums[idx]%2==0 and init%2!=0: _sum+=nums[idx]
            elif nums[idx]%2!=0 and init%2==0: _sum-=init
            elif nums[idx]%2==0 and init%2==0: _sum+=(nums[idx] - init)
            ans.append(_sum)
        return ans

        
        

        