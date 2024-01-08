class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        while i<=j:
            if nums[i]==val:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
                continue
            i+=1
        return i
             
        