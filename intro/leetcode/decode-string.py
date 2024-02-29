class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        string = ''
        n = ''
        for i in range(len(s)):
            if s[i] == '[':
                stack.append((string, int(n)))
                string = ''
                n = ''
            elif s[i].isnumeric():
                n += s[i]
            
            elif s[i]!=']':
                string += s[i]
            elif s[i] == ']':
                k = stack.pop()
                string *= int(k[1])
                string = k[0] + string
        
        return string



