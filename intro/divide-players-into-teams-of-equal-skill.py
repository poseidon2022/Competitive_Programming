class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        prev = 0
        i,j = 0, len(skill) - 1
        while i<j:
            tar = skill[i] + skill[j]
            if prev!=0 and tar!=prev: return -1
            ans+=skill[i] * skill[j]
            prev = tar
            i+=1
            j-=1
        
        return ans

        