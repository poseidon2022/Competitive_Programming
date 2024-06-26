# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        init = capacity
        ans = 0
        i = 0
        while i<len(plants):
            print(ans)
            if capacity<plants[i]:
                capacity = init
                ans+=2*i
                continue
            capacity-=plants[i]
            ans+=1
            i+=1
        return ans

        