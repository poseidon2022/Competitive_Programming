class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        target = max(candies)
        ans = []
        for i in candies:
            ans.append(True) if i+extraCandies>=target else ans.append(False) 

        return ans       