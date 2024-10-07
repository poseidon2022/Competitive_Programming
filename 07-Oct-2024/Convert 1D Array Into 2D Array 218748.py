# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original): return []
        ans = []
        lst = []
        for idx, val in enumerate(original):
            lst.append(val)
            if ((idx + 1) % n) == 0:
                ans.append(lst)
                lst = []
        
        return ans


        