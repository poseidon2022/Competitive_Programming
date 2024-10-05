# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        winners = defaultdict(int)
        for win, lose in matches:
            winners[win]+=1
            losers[lose]+=1

        win_ans = set()
        lose_ans = set()
        for one,two in matches:
            if winners[one]>0 and losers[one]==0:
                win_ans.add(one)
            if losers[two]==1:
                lose_ans.add(two)
            if losers[one]==1:
                lose_ans.add(one)
        
        return [sorted(list(win_ans)), sorted(list(lose_ans))]
        