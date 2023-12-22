class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        wanted = arr.index(max(arr))
        flag1 = False
        flag2 = False
        for i in range(0, wanted):
            flag1 = True
            if arr[i]>=arr[i+1]: return False
        
        for i in range(wanted,len(arr)-1):
            flag2 = True
            if arr[i]<=arr[i+1]: return False
        
        if not flag1 or not flag2: return False
        return True

        