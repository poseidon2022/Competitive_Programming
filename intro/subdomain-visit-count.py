class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        mine = defaultdict(int)
        ans = []
        for i in cpdomains:
            o, web = i.split(' ')
            o = int(o)
            mine[web]+=o
            for i in range(len(web)-1, -1,-1):
                if web[i]=='.':
                    mine[web[i+1:]]+=o
        
        for i in mine:
            ans.append(str(mine[i]) + ' ' + i)
        
        return ans
