class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(' ')
        arr.sort(key = lambda x: x[-1])
        print(arr)
        ans = ''
        for i in arr:
            ans+=i[:-1] + ' '
        
        return ans.rstrip()
        