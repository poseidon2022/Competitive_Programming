# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mine = defaultdict(int)
        for i in arr:
            mine[i%k] += 1
        
        count = 0
        for i in arr:
            target = -i % k
            if mine[target]:
                mine[target] -= 1
                if mine[i % k]:
                    mine[i % k] -= 1
                    count += 1

        return count == len(arr) // 2
        