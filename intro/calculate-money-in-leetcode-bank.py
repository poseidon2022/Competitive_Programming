class Solution:
    def totalMoney(self, n: int) -> int:

        total = 0
        monday_count = 0
        normal_days = 0

        for i in range(n):

            if i%7==0:
                if i==0: monday_count = 1
                else: monday_count = i//7 + 1
                normal_days = monday_count + 1
                total+=monday_count
                continue

            total+=normal_days
            normal_days+=1
        
        return total
            
        