class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = float('inf')
        sta, end = 0, -1
        counter = Counter(t)
        mine = defaultdict(int)
        anot = defaultdict(int)
        l,r = 0,0
        while r<len(s):
            if counter[s[r]]:
                if mine[s[r]]<counter[s[r]]: mine[s[r]]+=1
                else: anot[s[r]]+=1
            while mine==counter:
                if counter[s[l]]:
                    if not anot[s[l]]: mine[s[l]]-=1
                    else: anot[s[l]]-=1
                if r-l+1<ans:
                    ans = r - l + 1
                    sta, end = l, r
                l+=1
                
                
            r+=1

        print(sta, end)
        return s[sta:end+1]   
