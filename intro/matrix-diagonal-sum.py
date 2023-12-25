class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        _sum = 0
        while i<len(mat):
            _sum+=mat[i][i]
            i+=1
        i,j = 0,len(mat)-1
        while i<len(mat):
            if i!=j: _sum+=mat[i][j]
            i+=1
            j-=1
        return _sum
        