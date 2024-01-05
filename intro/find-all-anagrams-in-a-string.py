class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        target = Counter(p)
        mine = Counter()
        ans = []
        i,j = 0,0
        while j<len(s):
            mine[s[j]]+=1
            if j-i+1==len(p):
                if mine==target: ans.append(i)
                mine[s[i]]-=1
                i+=1
            j+=1
        return ans

        