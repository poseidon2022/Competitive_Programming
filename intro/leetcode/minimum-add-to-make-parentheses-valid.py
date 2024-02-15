class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0 
        cl = 0
        for i in range(len(s)):
            if s[i]=='(': op += 1
            elif s[i]==')' and op: op -= 1
            else: cl += 1

        return op + cl     