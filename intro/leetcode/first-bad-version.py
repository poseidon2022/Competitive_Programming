# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        sta = 1
        end = n
        while sta < end:
            mid = (sta + end)//2
            wanted = isBadVersion(mid)
            if not wanted: sta = mid + 1
            else: end = mid
        
        return sta
        