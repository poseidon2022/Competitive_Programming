class Solution:
    def largestGoodInteger(self, num: str) -> str:

        i,j = 0,0
        ans = '0'
        while j<len(num):
            if num[i]!=num[j]:
                if j-i>=3 and int(num[i]*3)>=int(ans): ans = num[i]*3
                i = j
            j+=1
        if j-i>=3 and int(num[i]*3)>=int(ans): ans = num[i]*3
        return ans if len(ans)>1 else ''
             
        