class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges,key = lambda x: x[1])
        n = max(right+1,ranges[len(ranges)-1][1] + 1)
        inter = [0]*n
        for sta,end in ranges:
            inter[sta]+=1
            if end+1<n: inter[end+1]-=1
        pref = [0]*len(inter)
        pref[0] = inter[0]
        for i in range(1,len(pref)): pref[i] = pref[i-1] + inter[i]


        for i in range(left,right+1):
            if pref[i]==0: return False
        return True