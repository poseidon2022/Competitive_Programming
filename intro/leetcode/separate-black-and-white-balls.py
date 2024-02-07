class Solution:
    def minimumSteps(self, s: str) -> int:

        s = list(s)
        l, r = 0, 0
        ans = 0
        while r<len(s):
            if s[l]!='1':
                while l<len(s) and s[l]!='1':
                    l += 1
                    r = l
                continue
            elif s[r]=='0':
                ans += r - l
                s[r], s[l] = s[l], s[r]
                l+=1
            r+=1
        
        return ans
            
        
        