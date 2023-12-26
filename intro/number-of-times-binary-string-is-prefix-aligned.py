class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        flip = 0
        count = 0
        _max = float('-inf')
        for i in flips:
            flip+=1
            _max = max(_max,i)
            if flip==_max: count+=1
        
        return count

        