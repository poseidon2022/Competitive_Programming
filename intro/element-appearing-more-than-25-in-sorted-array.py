class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        mine = defaultdict(int)
        for i in arr:
            mine[i]+=1
        
        for i in mine:
            if mine[i] > (0.25)*(n):
                return i
        