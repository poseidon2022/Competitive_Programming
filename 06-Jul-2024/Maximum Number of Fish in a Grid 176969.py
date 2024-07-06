# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        visited = set()
        def bounded(row, col):
            return 0 <= row < n and 0 <= col < m

        def helper(row, col):
            queue = deque([(row, col)])
            ans = grid[row][col]
            while queue:
                curRow, curCol = queue.popleft()
                for r, c in [(curRow + 1, curCol), (curRow, curCol + 1),(curRow - 1, curCol), (curRow, curCol - 1)]:
                    if bounded(r,c) and grid[r][c] and (r, c) not in visited and (r,c) != (row, col):
                        visited.add((r,c))
                        queue.append((r,c))
                        ans += grid[r][c]

            return ans


        final = 0
        for row in range(n):
            for col in range(m):
                if (row, col, grid[row][col]) not in visited and grid[row][col]:
                    visited.add((row, col))
                    final = max(final, helper(row, col))
        
        return final
