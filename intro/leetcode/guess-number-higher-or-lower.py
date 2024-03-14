# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        sta = 1
        end = n
        while sta <= end:
            mid = (sta + end) // 2
            cond = guess(mid)
            if cond == -1:
                end = mid - 1
            elif cond == 1:
                sta = mid + 1
            else:
                return mid
        
        return sta

        