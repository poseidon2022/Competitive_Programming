class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        _max = float('-inf')
        for i in range(len(grid[0])-2):
            for j in range(len(grid)-2):
                ans = sum(grid[j][i:i+3]) + grid[j+1][i+1] + sum(grid[j+2][i:i+3])
                _max = max(ans, _max)
        
        return _max


        