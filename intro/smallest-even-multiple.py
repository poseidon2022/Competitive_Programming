class Solution:
    def smallestEvenMultiple(self, n: int) -> int:

        ans = n
        while ans%2!=0 or ans%n!=0: ans+=1
        return ans
        