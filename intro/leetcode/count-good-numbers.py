class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        MOD = 10**9 + 7
        def fast(a, n):
            if n==0:
                return 1
            
            if n%2 == 0:
                return fast((a * a) % (10**9 + 7), n//2)
            return a * fast((a*a)%(10** 9 + 7), (n-1)//2)
        
        return (fast(5, (n+1)//2) * fast(4, n//2)) % MOD
        

        