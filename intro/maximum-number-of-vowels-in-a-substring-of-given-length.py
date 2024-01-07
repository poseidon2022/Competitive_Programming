class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0,0
        v_count = 0
        ans = 0
        checker = ('a','e','i','o','u')
        while r<len(s):
            if s[r] in checker: v_count+=1
            if r-l+1==k:
                ans = max(ans,v_count)
                if s[l] in checker: v_count-=1
                l+=1
            r+=1
        
        return ans


        