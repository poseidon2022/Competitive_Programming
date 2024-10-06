# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        flip_count = 0
        for shift in range(32):
            if (1 & (start >> shift)) != (1 & (goal >> shift)):
                flip_count += 1
        
        return flip_count