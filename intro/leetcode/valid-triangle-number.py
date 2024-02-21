class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 3: return 0
        ans = 0
        for i in range(len(nums) - 1, 0, -1):
            large_side = nums[i]
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > large_side:
                    ans += r - l
                    r -= 1
                    continue
                l += 1
        
        return ans



       

        

        