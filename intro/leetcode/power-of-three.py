class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def checker(num):
            if num%3==0 and num!=0:
                num = num/3
                return checker(num)
            return num==1
        return checker(n)