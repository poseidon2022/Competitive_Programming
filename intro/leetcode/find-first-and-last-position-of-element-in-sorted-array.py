class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sta = 0
        end = len(nums)-1
        if not nums: return [-1,-1]
        ans = []
        while sta <= end:

            mid = (sta + end) // 2
            if nums[mid] < target:
                sta = mid + 1
            else:
                end = mid - 1
    
        if sta<len(nums) and nums[sta] == target:
            ans.append(sta)
        sta, end = 0, len(nums) - 1
        while sta <= end:
            mid = (sta + end) // 2
            if nums[mid] <= target:
                sta = mid + 1
            else:
                end = mid - 1
        if end<len(nums) and nums[end] == target:
            ans.append(end)
        
        print(ans)
        return [-1,-1] if not ans else ans
        
        