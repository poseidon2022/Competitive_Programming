class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pref = [[0 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]
        self.matrix = matrix
        self.pref[0][0] = self.matrix[0][0]
        for i in range(1, len(matrix[0])):
            self.pref[0][i] = self.pref[0][i-1] + self.matrix[0][i]
        for j in range(1, len(matrix)):
            self.pref[j][0] = self.pref[j - 1][0] + self.matrix[j][0]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.pref[i][j] = self.pref[i-1][j] + self.pref[i][j-1] - self.pref[i-1][j-1] + self.matrix[i][j]
        
        print(self.pref)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1!=0: return self.pref[row2][col2] - self.pref[row2][col1-1]
        elif row1!=0 and col1==0: return self.pref[row2][col2] - self.pref[row1-1][col2]
        elif row1==0 and col1==0: return self.pref[row2][col2]
        return self.pref[row2][col2] - self.pref[row1-1][col2] - self.pref[row2][col1-1] + self.pref[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)