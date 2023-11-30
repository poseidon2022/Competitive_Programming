class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i])):
                target = matrix[i][j]
                if j+1<len(matrix[i+1]) and target!=matrix[i+1][j+1]: return False
            
        return True


