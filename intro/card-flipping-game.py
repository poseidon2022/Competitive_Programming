class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        up = defaultdict(list)
        down = defaultdict(list)
        for i in range(len(fronts)):
            up[fronts[i]].append(i)
            down[backs[i]].append(i)
        
        ans = float('inf')
        for i in up:
            flag = False
            for j in up[i]:
                if j in down[i]:
                    flag = True
                    break
            if not flag: ans = min(ans,i)
        
        for i in down:
            flag = False
            for j in down[i]:
                if j in up[i]:
                    flag = True
                    break
            if not flag: ans = min(ans,i)
        
        return ans if ans!=float('inf') else 0