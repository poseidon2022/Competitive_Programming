class Solution:
    def exist(self, board: List[List[str]], s: str) -> bool:

        s = s[::-1]
        def bounded(row, column):
            return 0 <= row < len(board) and 0 <= column < len(board[0])
    
        
        final = set()
        def helper(formed, visited, r, c, index):

            if len(formed) == len(s) or (formed and formed[-1]!=s[index]):
                final.add(formed)
                return

            formed += board[r][c]
            visited.add((r, c))
            for i, j in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
                if bounded(i, j) and (i,j) not in visited:
                    visited.add((i, j))
                    helper(formed, visited, i, j, index + 1)
                    visited.remove((i, j))
            
            final.add(formed)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                helper('', set(), i, j, -1)
        


        return s in final
