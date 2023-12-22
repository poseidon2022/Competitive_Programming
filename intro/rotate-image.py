class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
           for j in range(i, len(matrix)):
               matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            j, k = 0, len(matrix[i])-1
            while j<k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j+=1
                k-=1