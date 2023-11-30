class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        _num = 0
        for i in range(16, -1, -1):
            print(_num)
            if _num==n: break
            elif (_num + 2*(3**i) < n): return False
            elif _num + (3**i) <= n: _num = _num + 3**i
            
        
        return True if _num==n else False