class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def checker(c,k):

            l, r = 0, 0
            ans = 0
            while r<len(answerKey):
                if answerKey[r]!=c: k-=1
                while k==-1:
                    ans = max(ans,r-l)
                    if answerKey[l]!=c: k+=1
                    l+=1
                r+=1

            return max(ans,r-l)

        
        return max(checker('T',k), checker('F',k))

        