class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        ans = 0
        while maxDoubles and target!=1:
            rem = target%2
            target = target//2
            maxDoubles-=1
            if rem: ans+=1
            ans+=1
        
        ans+=(target - 1)
        return ans

        