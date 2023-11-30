class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        i = 0
        while i<len(strs[0]):
            start = strs[0][i]
            for j in strs:
                if i>=len(j) or j[i]!=start: return ans

            ans+=strs[0][i]
            i+=1
        return ans
            
            

            
            

