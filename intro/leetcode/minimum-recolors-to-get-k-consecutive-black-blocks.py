class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        l, r = 0, 0
        recol = 0
        ans = float('inf')
        bla = 0
        while r<n:
            if blocks[r]=='W': recol+=1
            bla+=1
            if bla==k:
                ans = min(ans,recol)
                if blocks[l]=='W': recol-=1
                bla-=1
                l+=1
            r+=1
        
        return ans
            
        