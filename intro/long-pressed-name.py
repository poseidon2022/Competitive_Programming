class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        if len(name)> len(typed): return False
        i,j = 0,0
        prev = name[0]
        while i<len(name) and j<len(typed):
            if name[i]==typed[j]:
                prev = name[i]
                i+=1
                j+=1
            if i>=len(name): break
            while j<len(typed) and name[i]!=typed[j]:
                if typed[j]!=prev: return False
                j+=1
        if i>=len(name):
            while j<len(typed):
                if typed[j]!=name[-1]: return False
                j+=1
        return True if i>=len(name) and j>=len(typed) else False