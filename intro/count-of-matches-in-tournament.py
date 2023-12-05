class Solution:
    def numberOfMatches(self, n: int) -> int:

        ans = 0
        while n!=1:
            ans = ans + n//2 if n%2==0 else ans + (n//2 + 1)
            n = n//2
        return ans

        