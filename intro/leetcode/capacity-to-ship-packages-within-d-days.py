class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        ans = float('inf')
        while low <= high:

            mid = (low + high) // 2
            d = 1
            _sum = 0
            for i in range(len(weights)):
                _sum += weights[i]
                if _sum > mid:
                    d += 1
                    _sum = weights[i]
            if d > days:
                low = mid + 1
            else:
                ans = min(ans, mid)
                high = mid - 1
        
        return ans

        