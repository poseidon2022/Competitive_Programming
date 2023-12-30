class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        j = len(piles)-2
        ans = 0
        while j>i:
            ans+=piles[j]
            j-=2
            i+=1
        
        return ans
