# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        memo = {}
        def helper(row, col):
            if row == len(dungeon) or col == len(dungeon[0]):
                return float('-inf')
            if row == len(dungeon)-1 and col == len(dungeon[0])-1:
                return dungeon[row][col] if dungeon[row][col] < 0 else 0
            
            if (row,col) not in memo:
                val1 = helper(row + 1, col)
                val2 = helper(row, col + 1)
                if val1 + dungeon[row][col] > 0:
                    val1 = 0
                else:
                    val1 += dungeon[row][col]
                if val2 + dungeon[row][col] > 0:
                    val1 = 0
                else:
                    val2 += dungeon[row][col]

                memo[(row, col)] = max(val1, val2)
            return memo[(row,col)]
        
        start = helper(0,0)
        return -start + 1 if start<0 else 1

        