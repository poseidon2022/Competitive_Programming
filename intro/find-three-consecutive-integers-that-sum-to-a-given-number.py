class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        target = num//3
        ans = []
        if (target-1) + (target) + (target+1) == num:
            ans = [target-1,target, target+1]
         
        
        return ans
        
        