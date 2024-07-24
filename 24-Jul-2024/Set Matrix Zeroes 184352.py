# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for row in range(n):
            for col in range(m):
                if not matrix[row][col]: matrix[row][col] = "#"
        

        for row in range(n):
            for col in range(m):
                if matrix[row][col] == '#':
                    matrix[row][col] = 0
                    for i in range(n):
                        if matrix[i][col]!="#": matrix[i][col] = 0
                    for j in range(m):
                        if matrix[row][j]!="#": matrix[row][j] = 0

