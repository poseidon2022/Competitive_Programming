# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        def search(cur):
            low, high = 0, len(profit) - 1
            highest = 0
            while low <= high:

                mid = (low + high) // 2
                if dif_prof[mid][0] > cur:
                    high = mid - 1
                
                else:
                    low = mid + 1
                    highest = max(highest, dif_prof[mid][1])
            
            return highest
        
        dif_prof = [[difficulty[i], profit[i]] for i in range(len(profit))]
        dif_prof.sort()
        best_profit = 0
        for i in range(len(profit)):
            best_profit = max(best_profit, dif_prof[i][1])
            dif_prof[i][1] = best_profit
        
        ans = 0
        for person in worker:
            salary = search(person)
            ans += salary
        
        return ans
            
        


