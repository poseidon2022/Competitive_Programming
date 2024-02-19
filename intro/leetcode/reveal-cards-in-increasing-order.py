class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        ans = deque()
        ans.append(deck[-1])
        for i in range(len(deck)-2,-1,-1):
            k = ans.pop()
            ans.appendleft(k)
            ans.appendleft(deck[i])
        
        return ans
        

        