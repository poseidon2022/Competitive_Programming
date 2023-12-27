class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = float('-inf')
        anot = []
        for i,j in points: anot.append(i)
        anot.sort()
        for i in range(1,len(anot)):
            ans = max(ans, anot[i] - anot[i-1])
        
        return ans
