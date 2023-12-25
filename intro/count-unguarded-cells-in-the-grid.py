class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        subtracted = len(guards) + len(walls)
        total = m*n - subtracted
        walls_copy = set()
        guards_copy = set()
        guarded = set()
        for i,j in walls: walls_copy.add((i,j))
        for i,j in guards: guards_copy.add((i,j))
        for x,y in guards:
            i,j = x-1,y 
            while i>=0:
                if (i,j) not in guards_copy and (i,j) not in walls_copy:
                    guarded.add((i,j))
                else: break
                i-=1
            i,j = x+1,y 
            while i<m:
                if (i,j) not in guards_copy and (i,j) not in walls_copy:
                    guarded.add((i,j))
                else: break
                i+=1
            i,j = x,y-1 
            while j>=0:
                if (i,j) not in guards_copy and (i,j) not in walls_copy:
                    guarded.add((i,j))
                else: break
                j-=1
            i,j = x,y+1 
            while j<n:
                if (i,j) not in guards_copy and (i,j) not in walls_copy:
                    guarded.add((i,j))
                else: break
                j+=1
        print(total)
        print(guarded)
        return total - len(guarded)
            
            

            
                

