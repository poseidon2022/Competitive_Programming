class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mine = {'2':'abc','3':'def','4':'ghi', '5':'jkl','6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = []
        def helper(s,i):
            if len(s) == len(digits):
                if s: ans.append(s)
                return
            
            for letter in mine[digits[i]]:
                helper(s + letter, i + 1)
        
        helper('', 0)
        return ans


            
            
        