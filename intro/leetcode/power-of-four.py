class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        def power(n):
            if n==0: return False
            if n==1 or n%4!=0:
                if n==1: return True
                else: return False
            
            return power(n//4)
        
        return power(n)
        