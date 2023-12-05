class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse =True)
        large = 0
        small = 1
        ans = 0
        print(nums)
        while small<len(nums)-1:
            if nums[small] + nums[small+1] > nums[large]:
                return nums[small] + nums[small+1] + nums[large]
            
            small+=1
            large+=1
        
        return ans
        
                
        
        