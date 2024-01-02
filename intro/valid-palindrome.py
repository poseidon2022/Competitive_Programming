class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i<=j:
            if not (s[i].isalpha() or s[i].isdigit()) or not (s[j].isalpha() or s[j].isdigit()):
                if not (s[i].isalpha() or s[i].isdigit()): i+=1
                if not (s[j].isalpha() or s[j].isdigit()): j-=1
            elif s[j].lower()!=s[i].lower():
                return False
            else:
                i+=1
                j-=1
        
        return True