class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        for i in range(min(len(word1), len(word2))):
            ans+=word1[i] + word2[i]
        
        i+=1
        while i<len(word1):
            ans+=word1[i]
            i+=1
        while i<len(word2):
            ans+=word2[i]
            i+=1
        
        return ans

        