# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        magic_number = n - 1
        if time >= n:
            if (time // magic_number) % 2 == 0:
                return time%magic_number + 1
            return n - (time%magic_number)
        return time + 1
        