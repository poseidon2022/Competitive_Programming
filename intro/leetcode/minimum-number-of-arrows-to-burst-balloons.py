class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        ans = 1
        ran = points[0]
        for i in range(1, len(points)):
            if (points[i][0] >= ran[0]) and (points[i][0] <= ran[1]):
                ran = [ran[0], min(ran[1], points[i][1])]
                continue
            ans+=1
            ran = points[i]
        
        return ans
        

        