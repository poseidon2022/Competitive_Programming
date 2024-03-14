class Solution:
    def mySqrt(self, x: int) -> int:

        sta = 1
        end = x
        while sta <= end:
            mid = (sta + end) // 2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                sta = mid + 1
            else:
                return mid
        
        return end

        