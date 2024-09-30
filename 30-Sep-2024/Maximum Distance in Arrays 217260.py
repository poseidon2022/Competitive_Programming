# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        _max, _min = arrays[0][-1], arrays[0][0]
        ans = 0
        for idx in range(1,len(arrays)):
            ans = max(ans, _max - arrays[idx][0], arrays[idx][-1] - _min)
            _max = max(_max, arrays[idx][-1])
            _min = min(_min, arrays[idx][0])
        
        return ans
        
        