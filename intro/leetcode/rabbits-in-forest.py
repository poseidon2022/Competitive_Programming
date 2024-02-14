class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        mine = defaultdict(int)
        ans = 0
        for i in answers:
            if not mine[i]: mine[i] = i
            else: mine[i]-=1
            ans+=1
        
        for i in mine: ans+=mine[i]
        
        return ans
        