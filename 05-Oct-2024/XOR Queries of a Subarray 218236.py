# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        pref = [0 for _ in range(len(arr))]
        pref[0] = arr[0]
        for idx in range(1, len(arr)):
            pref[idx] = pref[idx-1] ^ arr[idx]
        
        ans = []
        for sta, end in queries:
            if sta == 0: ans.append(pref[end])
            else: ans.append(pref[end] ^ pref[sta-1])
        
        return ans
        