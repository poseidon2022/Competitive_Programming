# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mine = defaultdict(list)
        ans = []
        for i in strs:
            let = tuple(sorted(list(i)))
            mine[let].append(i)
        
        for j in mine:
            ans.append(mine[j])
        return ans

    