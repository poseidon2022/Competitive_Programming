class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        l, r = 0,0
        mine = defaultdict(int)
        ans = float('inf')
        while r<n:
            mine[cards[r]]+=1
            while len(mine)<r-l+1:
                ans = min(ans, r-l+1)
                mine[cards[l]]-=1
                if not mine[cards[l]]: del mine[cards[l]]
                l+=1
            r+=1

        return -1 if ans==float('inf') else ans       