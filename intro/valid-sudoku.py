class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = defaultdict(int)
            column = defaultdict(int)
            for j in range(9):
                if row[board[i][j]]==1: return False
                if board[i][j]!='.': row[board[i][j]]+=1
                if column[board[j][i]]==1: return False
                if board[j][i]!='.': column[board[j][i]]+=1
        
        ans = [[] for _ in range(3)]
        for i in range(9):
            ans[0].extend(board[i][0:3])
            ans[1].extend(board[i][3:6])
            ans[2].extend(board[i][6:9])
            if len(ans[0])==9:
                for i in ans:
                    with_in = defaultdict(int)
                    for j in i:
                        if with_in[j]==1: return False
                        if j!='.': with_in[j]+=1
                ans = [[] for _ in range(3)]
        
        
        return True
