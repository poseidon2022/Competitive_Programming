class Solution:
    def totalNQueens(self, n: int) -> int:
        
        ans = []
        def helper(arr, r, l_diag, r_diag, visited_col):
            if len(arr) == n:
                ans.append(arr[:])
                return
            
            for col in range(n):
                
                if (r - col not in r_diag) and (r + col not in l_diag) and (col not in visited_col):
                    l_diag.add(r + col)
                    r_diag.add(r - col)
                    visited_col.add(col)
                    arr.append('.' * col + 'Q' + '.' * (n - col - 1))
                    helper(arr, r + 1, l_diag, r_diag, visited_col)
                    l_diag.remove(r + col)
                    r_diag.remove(r - col)
                    visited_col.remove(col)
                    arr.pop()
            
        helper([], 0, set(),set(), set())
        return len(ans)