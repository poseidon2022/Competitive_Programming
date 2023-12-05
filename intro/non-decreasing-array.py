class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        if len(nums)==1 or (len(nums)==2 and nums[-1]>nums[0]): return True
        _max = nums[0]
        flag = False
        for i in range(len(nums)):
            if i-1<0: prev = float('-inf')
            else: prev = nums[i-1]
            if i-2<0: prev_prev = float('-inf')
            else: prev_prev = nums[i-2]

            if not flag and (nums[i]<prev):
                if nums[i]>=prev_prev: nums[i-1] = nums[i]
                else: nums[i] = max(prev,prev_prev)
                flag = not flag
            elif flag and (nums[i]<prev): return False


                
        return True        