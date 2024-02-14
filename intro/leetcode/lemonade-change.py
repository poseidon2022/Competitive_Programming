class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        mine = defaultdict(int)
        for i in range(len(bills)):
            mine[bills[i]] += 1
            if bills[i] == 10:
                if not mine[5]: return False
                mine[5] -= 1
            elif bills[i] == 20:
                if mine[5] and mine[10]:
                    mine[5] -= 1
                    mine[10] -= 1
                elif mine[5] >= 3: mine[5] -= 3
                else: return False

        
        return True