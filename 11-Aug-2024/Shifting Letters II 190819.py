# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        inter = [0 for _ in range(len(s))]
        for sta, end, dxn in shifts:
            if dxn==1:
                inter[sta]+=1
                if end+1<len(s): inter[end+1]-=1
            else:
                inter[sta]-=1
                if end+1<len(s): inter[end+1]+=1

        
        pref = [0 for _ in range(len(inter))]
        pref[0] = inter[0]
        for i in range(1, len(pref)):
            pref[i] = pref[i-1] + inter[i]
        
        ans = ''
        print(pref)
        for i in range(len(s)):
            tar = (ord(s[i]) - 97 + pref[i]) % 26
            shifted_char = chr(tar + 97)
            ans += shifted_char
        
        return ans



