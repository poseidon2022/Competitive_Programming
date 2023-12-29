class Solution:
    def smallestNumber(self, num: int) -> int:
        if len(str(num))==1: return num
        if num<0:
            num = str(num)
            num = list(map(int, num[1:]))
            num.sort(reverse = True)
            const = ''
            for i in num: const+=str(i)
            return -int(const)
        
        else:
            num = str(num)
            mine = []
            for i in num:
                if i!='0': mine.append(i)
            zeroes = num.count('0')
            mine.sort()
            ans = mine[0] + zeroes*'0' + ''.join(mine[1:])
            return int(ans)