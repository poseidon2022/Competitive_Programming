class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for idx, val in enumerate(costs):
            coins-=val
            if coins<0: return idx
        
        return idx + 1
        