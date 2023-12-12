class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        mine = set()
        while n!='1':
            if n in mine: return False
            mine.add(n)
            _sum = 0
            for i in n: _sum+=int(i)**2
            n = str(_sum)

        
        return True
