class Solution:
    def balancedString(self, s: str) -> int:

        e = len(s)//4
        l, r =  0, 0
        mine = defaultdict(int)
        for i in s: mine[i]+=1

        ans = float('inf')
        while r < len(s)+1:
            
            print(l, r, mine)
            while all(mine[i]<=e for i in mine):
                ans = min(ans, r - l)
                if l==r: return 0
                mine[s[l]]+=1
                if not mine[s[l]]: del mine[s[l]]
                l+=1
            
            if r<len(s): mine[s[r]]-=1
            r+=1
        
        return ans if ans!=float('inf') else 0







        


        