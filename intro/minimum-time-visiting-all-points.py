class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        ans = 0
        for i in range(len(points)-1):
            x1,y1 = points[i]
            x2,y2 = points[i+1]
            if ((x1-x2)**2 + (y1 - y2)**2)**0.5==(2)**0.5: ans+=1
            else: ans+=max(abs(x1-x2),abs(y1-y2))
        
        return ans

            
        