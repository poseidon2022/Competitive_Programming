class Solution:
    def printVertically(self, s: str) -> List[str]:

        arr = s.split (' ')
        ans = []
        target = sorted(arr, key = lambda x: len(x), reverse = True)[0]
        for i in range(len(target)):
            temp = ''
            for j in range(len(arr)):
                if i<len(arr[j]): temp+=arr[j][i]
                else: temp+=' '
            ans.append(temp.rstrip())
        
        return ans
        