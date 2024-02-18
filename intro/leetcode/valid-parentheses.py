class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        for i in range(len(s)):
            
            if s[i]==']':
                if not sta or sta[-1]!='[': return False
                sta.pop()
            elif s[i]=='}':
                if not sta or sta[-1]!='{': return False
                sta.pop()
            elif s[i]==')':
                if not sta or sta[-1]!='(': return False
                sta.pop()
            else: sta.append(s[i])
        
        return not sta
            

        
        return True
        