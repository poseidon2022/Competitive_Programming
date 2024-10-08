# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r<len(nums):
            if nums[l]!=nums[r]:
                nums[l+1], nums[r] = nums[r], nums[l+1]
                l+=1
            
            r+=1
        return l+1
    
        