class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            target = digits[i] + 1
            if target==10 and i==0:
                digits[i] = 0
                return [1] + digits
            elif target==10: digits[i]=0
            else:
                digits[i] = target
                return digits

            