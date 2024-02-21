class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        sta = []
        temp = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if temp > nums[i]: return True
            while sta and sta[-1] < nums[i]:
                temp = sta.pop()
            
            sta.append(nums[i])
        
        return False


            
        