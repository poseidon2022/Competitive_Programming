class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        mine = defaultdict(int)
        for i in range(len(s)): mine[s[i]] = i

        l, r = 0, 0
        cur = 0
        ans = []
        while r < len(s):
            cur = max(cur, mine[s[r]])
            if r == cur:
                ans.append(r - l + 1)
                l = r + 1
            r+=1
        
        return ans
        