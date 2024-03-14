class Solution:
    def findMin(self, nums: List[int]) -> int:

        sta = 0
        end = len(nums) - 1
        ans = float('inf')
        while sta <= end:

            mid = (sta + end) // 2
            if nums[mid] > nums[end]:
                sta = mid + 1
            else:
                end = mid - 1
            ans = min(ans, nums[mid])
            
        return ans

        