class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        mine = defaultdict()
        for i in range(97,123):
            if i<106: mine[str(i-96)] = chr(i)
            else:
                mine[str(i-96) + '#'] = chr(i)

        ans = ''
        print(mine)
        i = 0
        while i<len(s):
            if i+2<len(s) and s[i:i+3] in mine:
                ans+=mine[s[i:i+3]]
                i+=3
                continue
            ans+=mine[s[i]]
            i+=1
        return ans






        