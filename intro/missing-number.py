class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==mid: i = mid + 1
            elif nums[mid]>mid: j = mid - 1
        return i
        
