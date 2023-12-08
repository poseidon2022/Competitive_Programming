class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        mine = defaultdict(list)
        for i in paths:
            pref = i[:i.index(' ')]
            target = i.split(' ')
            for j in target[1:]:
                f = j[:j.index('(')]
                content = j[j.index('(')+1:j.index(')')]
                mine[content].append(pref + '/' + f)
        
        print(mine)
        for i in mine:
            if len(mine[i])>=2: ans.append(mine[i])
        
        return ans
        

        