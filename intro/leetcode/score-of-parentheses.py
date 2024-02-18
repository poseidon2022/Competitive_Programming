class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        ans = 0
        sta = []
        f = False
        for i in range(len(s)):
            if s[i]=='(': sta.append(s[i])
            else:
                if s[i - 1]=='(': ans += 2 ** (len(sta) - 1)
                sta.pop()
        
        return ans
        