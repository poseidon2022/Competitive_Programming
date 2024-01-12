class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mine = set(s)
        self.ans = float('-inf')
        def custom(c, d):
            l, r = 0, 0
            while r<len(s):
                if s[r]!=c: d-=1
                while d<0:
                    if s[l]!=c: d+=1
                    l+=1

                self.ans = max(self.ans, r-l+1)
                r+=1
            
        for i in mine: custom(i, k)
        
        return self.ans


        