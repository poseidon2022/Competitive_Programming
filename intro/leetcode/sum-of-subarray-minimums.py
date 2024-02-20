class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sta = []
        ans = [1 for _ in range(len(arr))]
        for i in range(len(arr)):
            
            while sta and sta[-1][1] > arr[i]:
                ans[sta[-1][0]] *= (i - sta[-1][0])
                sta.pop()
            
            if not sta: ans[i] *= i + 1
            else: ans[i] *= i - sta[-1][0]
            sta.append((i, arr[i]))

        while sta:
            ans[sta[-1][0]] *= len(arr) - sta[-1][0]
            sta.pop()
        
        final = 0
        for i in range(len(arr)):
            final += arr[i] * ans[i]
        
        return final % (10**9 + 7)
        

        