class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        _sum = 0
        _max = float('-inf')
        i,j = 0, 0
        while j<len(nums):
            while j-i+1<=k:
                _sum+=nums[j]
                j+=1
            _max = max(_max, _sum)
            _sum-=nums[i]
            i+=1
        return _max / k