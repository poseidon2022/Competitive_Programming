# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        low = 1
        high = target
        arthSum = 0
        while low < high:
            
            mid = (low + high) // 2
            arthSum = (mid*(mid + 1))//2
           
            if arthSum >= target:
                high = mid
            else: low = mid + 1
        
        arthSum = (low*(low + 1))//2
        return low if abs(arthSum - target)%2 == 0 else low + (low%2) + 1
        