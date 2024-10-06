# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        ord_num = ""
        for let in s:
            ord_num += str(ord(let) - ord('a') + 1)
        
        while k:
            temp = sum([int(dig) for dig in ord_num])
            if k == 1: return temp
            ord_num = str(temp)
            k -= 1
        