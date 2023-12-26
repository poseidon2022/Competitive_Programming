class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mine = defaultdict(int)
        ans = []
        for i in range(len(names)):
            mine[heights[i]] = names[i]
        
        for i in range(len(heights)):
            j = i
            while j>0:
                if heights[j]>heights[j-1]:
                    heights[j], heights[j-1] = heights[j-1], heights[j]
                j-=1
            
        for i in heights:
            ans.append(mine[i])
        
        return ans
    
        