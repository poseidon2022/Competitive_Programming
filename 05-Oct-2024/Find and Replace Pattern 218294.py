# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        mine = defaultdict(str)
        word = defaultdict(str)
        ans = []
        for i in words:
            flag = True
            for j in range(len(i)):
                if (mine[pattern[j]] and i[j]!=mine[pattern[j]]) or (word[i[j]] and pattern[j]!=word[i[j]]):
                    flag = not flag
                    break
                mine[pattern[j]] = i[j]
                word[i[j]] = pattern[j]
            
            mine = defaultdict(str)
            word = defaultdict(str)
            if flag: ans.append(i)
        
        return ans
            