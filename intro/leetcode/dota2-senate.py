class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        queue = deque(list(senate))
        rad = 0
        dota = 0
        while queue:
            if dota==len(queue): return 'Dire'
            if rad==len(queue): return 'Radiant'
            k = queue.popleft()
            if k=='D' and not rad:
                dota += 1
                queue.append(k)
            elif k=='D' and rad: rad -= 1
            elif k=='R' and dota: dota -= 1
            elif k=='R' and not dota:
                rad += 1
                queue.append(k)
        
                 
        
        
        