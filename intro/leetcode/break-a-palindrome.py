class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        ans = ''
        n = len(palindrome)//2
        f = True
        if len(palindrome)==1: return ''
        for i in range(n):
            if f and palindrome[i]!='a':
                ans += 'a'
                f = False
            else: ans += palindrome[i]

        for i in range(n, len(palindrome)):
            if f and i == len(palindrome) - 1:
                ans += 'b'
                break
            ans += palindrome[i]

        return ans