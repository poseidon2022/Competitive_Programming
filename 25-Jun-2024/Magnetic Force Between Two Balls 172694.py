# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = -1, position[-1] - position[0] + 1
        def check(x):

            placed = 1
            curr = position[0]
            for p in range(1, len(position)):
                if curr + x <= position[p]:
                    curr = position[p]
                    placed += 1
            
            return placed >= m
            
        while high - low > 1:

            mid = (low + high) // 2
            if check(mid):
                low = mid
            else:
                high = mid

        return low




        
                 