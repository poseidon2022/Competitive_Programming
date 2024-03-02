class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def checker(val,board,row, col):
            for i in range(len(board)):
                if board[(row//3)*3 + i//3][(col//3)*3 + i%3] == val:
                    return False
                if board[row][i] == val:
                    return False
                if board[i][col] == val:
                    return False
                
            return True
        
        def helper(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':

                        for num in "123456789":

                            if checker(num, board, row, col):
                                board[row][col] = num
                                if helper(board):
                                    return True
                                else:
                                    board[row][col] = '.'
                        
                        return False
                
            return True

        helper(board)


        
        