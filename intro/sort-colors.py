class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        tar = 0
        while i<len(nums) - 1:
            j = i
            while j<len(nums) and nums[j]==tar: j+=1
            k = j+1
            while j<len(nums) and k<len(nums):
                if nums[k]==tar:
                    if nums[j]!=tar:
                        nums[j], nums[k] = nums[k], nums[j]
                        k+=1
                    j+=1
                else: k+=1
            i = nums.count(0)
            if tar==1: return 
            tar+=1




        