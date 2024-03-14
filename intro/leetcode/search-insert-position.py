class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        sta = 0
        end = len(nums) - 1
        while sta<=end:

            mid = (sta + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                sta = mid + 1
            else: return mid
        
        return sta
        