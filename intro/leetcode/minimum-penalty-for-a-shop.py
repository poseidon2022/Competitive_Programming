class Solution:
    def bestClosingTime(self, customers: str) -> int:

        sta = []
        ans = 0
        for i in range(len(customers)):
            if customers[i]=='Y': sta.append(1)
            else: sta.append(0)

        pref = [0 for _ in range(len(customers))]
        pref[0] = sta[0]
        for i in range(1, len(pref)):
            pref[i] = pref[i-1] + sta[i]
        
        pen = pref[-1]
        tar = pref[-1]
        for i in range(1,len(customers)):
            if customers[i-1]=='Y': tar-=1
            if customers[i-1]=='N': tar+=1
            if tar<pen:
                pen = tar
                ans = i
        
        if customers.count('N') < pen: ans = len(customers)
        return ans
            
        

        

        