class Solution:
    def numberOfWays(self, s: str) -> int:

        arr = list(map(int, s))
        pref = [0 for _ in range(len(s))]
        pref[0] = arr[0]
        
        for i in range(1, len(pref)):
            pref[i] = pref[i-1] + arr[i]
        
        zero_ones = []
        z = 0
        cur = 0
        for i in range(len(s)):
            if arr[i]==0: z+=1
            if arr[i]==1: cur+=z
            zero_ones.append(cur)
        
        
        final_one = 0
        for i in range(1,len(s)):
            m = (len(arr) - i - 1) - (pref[-1] - pref[i])
            if arr[i]==1: final_one += m * (zero_ones[i] - zero_ones[i-1])
        
        one_zeroes = []
        o = 0
        cur = 0
        for i in range(len(s)):
            if arr[i]==1: o+=1
            if arr[i]==0: cur+=o
            one_zeroes.append(cur)
        
        final_two = 0
        for i in range(1,len(s)):
            m = (pref[-1] - pref[i])
            if arr[i]==0: final_two += m * (one_zeroes[i] - one_zeroes[i-1])
        
        return final_one + final_two

        