class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        sta = []
        for i in tokens:
            if i not in operators: sta.append(i)
            else:
                if i=='/':
                    final = int(sta[-2])/int(sta[-1])
                    final = math.ceil(final) if final < 0 else math.floor(final)
                else:
                    temp = sta[-2] + i + sta[-1]
                    final = eval(temp)
                sta.pop()
                sta.pop()
                sta.append(str(final))

        return int(sta[-1])
        