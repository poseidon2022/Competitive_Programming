class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mine = defaultdict(int)
        ans = 0
        i,j = 0,0
        while j<len(s):
            mine[s[j]]+=1
            if mine[s[j]]==2:
                while mine[s[j]]==2:
                    mine[s[i]]-=1
                    if not mine[s[i]]: del mine[s[i]]
                    i+=1
            ans = max(ans, j-i+1)
            j+=1
        
        return ans
        