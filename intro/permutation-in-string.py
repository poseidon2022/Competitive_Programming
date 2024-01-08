class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        i,j = 0,0
        mine = defaultdict(int)
        while j<len(s2):
            if counter[s2[j]]: mine[s2[j]]+=1
            if j-i+1==len(s1):
                if mine==counter: return True
                mine[s2[i]]-=1
                if mine[s2[i]]<=0: del mine[s2[i]]
                i+=1
            j+=1        
        return False


        