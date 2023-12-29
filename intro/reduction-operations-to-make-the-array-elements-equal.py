class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = list(set(nums))
        nums.sort(reverse = True)
        target = nums.index(min(nums))
        ans = 0
        for idx,val in enumerate(nums):
            if (target - idx)>0: ans+=(target - idx) * counter[val]
            else: break
        
        return ans