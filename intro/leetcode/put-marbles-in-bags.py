class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        inter = []
        if len(weights) == 1:
            inter = weights
        for i in range(1, len(weights)):
            inter.append(weights[i] + weights[i - 1])
        inter.sort()
        print(inter)
        return -sum(inter[:k - 1]) + sum(inter[len(inter) - k + 1:])
        

      
      