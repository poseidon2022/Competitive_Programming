class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        trans = []
        for i in range(len(grid[0])):
            inter = []
            for j in range(len(grid)):
                inter.append(grid[j][i])
            trans.append(inter)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(max(grid[i]), max(trans[j])) - grid[i][j]
        
        return ans

        