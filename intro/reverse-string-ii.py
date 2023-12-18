class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0
        r = k
        s = list(s)
        while r<=len(s):
            s[l:r] = s[l:r][::-1]
            l+=2*k
            r = l+k
        if r-l+1>k:
            s[l:r] = s[l:r][::-1]
        return ''.join(s)
        