class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        inter = [0 for _ in range(n)]
        for f, l, s in bookings:
            inter[f - 1]+=s
            if l<len(inter): inter[l]-=s
        
        pref = [0 for _ in range(n)]
        pref[0] = inter[0]
        for i in range(1, n):
            pref[i] = pref[i-1] +  inter[i]
        
        return pref


        