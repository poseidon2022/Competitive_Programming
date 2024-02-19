class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        sta = []
        for i in range(len(temperatures)):
            while sta and sta[-1][0] < temperatures[i]:
                ans[sta[-1][1]] = i - sta[-1][1]
                sta.pop()
    
            sta.append((temperatures[i], i))
        
        return ans
        