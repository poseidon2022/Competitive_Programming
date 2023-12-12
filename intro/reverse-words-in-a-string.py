class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        i,j = 0,len(arr)-1
        ans = ""
        while i<j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        for i in arr: ans+=i + " "
        return ans.rstrip()
