class Solution:
    def interpret(self, command: str) -> str:

        ans = ''
        i = 0
        while i<len(command):
            if command[i]=='G': ans+='G'
            elif command[i]=='(' and command[i+1]==')': ans+='o'
            elif command[i]=='(' and command[i+1]=='a': ans+='al'
            i+=1
        return ans


        