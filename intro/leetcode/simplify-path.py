class Solution:
    def simplifyPath(self, path: str) -> str:
        mine = path.split('/')
        sta = ['/']
        for i in mine:
            if i=='..':
                while len(sta) > 1:
                    k = sta[-1]
                    sta.pop()
                    if k!='/': break

            elif i!='.' and i!='':
                if sta[-1]!='/': sta.append('/')
                sta.append(i)
        
        if len(sta) > 1 and sta[-1]=='/': sta.pop()
        return ''.join(sta)
            
            
            
        