# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        cost = [float('inf')] * n
        cost[src] = 0

        for i in range(k + 1): 

            temp_cost = cost.copy()
            for u, v, w in flights:
                if cost[u] != float('inf'):
                    temp_cost[v] = min(temp_cost[v], cost[u] + w)
            
            cost = temp_cost
            
        return cost[dst] if cost[dst] != float('inf') else -1