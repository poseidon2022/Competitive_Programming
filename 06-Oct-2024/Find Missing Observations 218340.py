# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        remaining = (mean * (len(rolls) + n)) - sum(rolls)
        if remaining / n > 6 or remaining < 0 or remaining // n == 0: return []

        missing = [remaining // n for _ in range(n)] 

        distr = remaining % n
        idx = 0
        while distr:
            missing[idx % len(missing)] += 1
            idx += 1
            distr -= 1
        
        return missing