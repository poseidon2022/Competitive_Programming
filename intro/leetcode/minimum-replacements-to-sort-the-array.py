class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = nums[-1]
        ans = 0
        for i in range(len(nums) - 2, -1, -1):

            bucket = math.ceil(nums[i] / n)
            ans += (bucket - 1)
            n = nums[i] // bucket
        
        return ans

        
        
        