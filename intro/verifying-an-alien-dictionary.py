class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        mine = defaultdict(int)
        for i in range(len(order)):
            mine[order[i]] = i+1
        if len(words)==1: return True
        for i in range(len(words)-1):
            one = words[i]
            two = words[i+1]
            j = 0
            while j<min(len(one), len(two)):
                if mine[one[j]]<mine[two[j]]: break
                elif mine[one[j]]==mine[two[j]]: j+=1
                elif mine[one[j]]>mine[two[j]]: return False
            
            if j==min(len(one), len(two)) and (len(one)>len(two)): return False
        
        return True
            