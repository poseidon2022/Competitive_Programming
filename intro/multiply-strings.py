class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiplier = num1[::-1]
        by = num2[::-1]
        total = 0
        for i in range(len(multiplier)):
            temp = int(multiplier[i])
            inter = ''
            carry = 0
            for j in range(len(by)):
                prod = temp* int(by[j]) + carry
                manip = str(prod)
                if j==len(by)-1:
                    inter+=manip[::-1]
                    break
                inter+=manip[-1]
                if len(manip)>1: carry = int(manip[0])
                else: carry = 0
            total+=int(inter[::-1] + i*'0')
        
        return str(total)

                