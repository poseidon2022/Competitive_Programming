class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def helper(s, o, c):

            if len(s) == 2*n:
                ans.append(s)
                return
            
            if o:
                helper(s + '(', o - 1, c)
                if o < c:
                    helper(s + ')', o, c - 1)

            elif c:
                helper(s + ')', o, c - 1)
            

        
        helper('', n, n)
        return ans
        