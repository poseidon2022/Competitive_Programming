# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        def bounded(row, col):
            return 0<=row<len(grid1) and 0<=col<len(grid1[0])
        
        visited = set()
        def checker(row, col):
            queue = deque([(row, col)])
            flag = True
            while queue:

                curRow, curCol = queue.popleft()
                for dx, dy in directions:
                    nextRow, nextCol = curRow + dx, curCol + dy
                    if bounded(nextRow, nextCol) and (nextRow, nextCol) not in visited and grid2[nextRow][nextCol] == 1:
                        if grid1[nextRow][nextCol] == 0: flag = False
                        visited.add((nextRow, nextCol))
                        queue.append((nextRow, nextCol))
                
            return flag
        
        ans = 0
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid2[row][col] == 1 and (row, col) not in visited and grid1[row][col] == 1:
                    visited.add((row, col))
                    if checker(row, col): ans += 1
            
        
        return ans
                    


