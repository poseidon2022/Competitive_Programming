class Solution:
    def romanToInt(self, s: str) -> int:

        mine = {'I':1,'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        i = 0
        ans = 0
        while i<len(s):
            if i+1<len(s) and s[i:i+2] in ("IV","IX","XL",'XC','CD','CM'):
                ans+=mine[s[i+1]] - mine[s[i]]
                i+=2
                continue
            
            ans+=mine[s[i]]
            i+=1
        
        return ans
                
                
            
        
        