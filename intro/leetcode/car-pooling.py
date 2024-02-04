class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        anot = sorted(trips, key = lambda x: -x[2])
        _max = anot[0][2]
        inter = [0 for _ in range(_max)]
        for p,s,e in trips:

            inter[s]+=p
            if e<len(inter): inter[e]-=p
        
        pref = [0 for _ in range(len(inter))]
        pref[0] = inter[0]
        for i in range(1,len(pref)):
            pref[i] = pref[i-1] + inter[i]
        
        print(pref)
        return all(i<=capacity for i in pref)
        