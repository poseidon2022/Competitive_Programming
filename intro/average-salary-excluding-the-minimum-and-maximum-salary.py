class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        i,j = 1,len(salary)-2
        ans = 0
        while i<=j:
            if i<j: ans+=salary[i] + salary[j]
            elif i==j and i>0: ans+=salary[i]
            i+=1
            j-=1
        return ans/(len(salary)-2)
        