class Solution:
    def longestPalindrome(self, s: str) -> int:

        count = Counter(s)
        ans = 0
        odd = []
        for i in count:
            if count[i]%2==0: ans+=count[i]
            if count[i]%2!=0: odd.append(count[i])
        
        odd.sort()
        if odd:
            ans += odd[-1]
            for i in range(len(odd) - 2, -1, -1):
                ans += odd[i] - 1
    
        return ans


        