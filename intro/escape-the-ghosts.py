class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        ghosts.sort(key = lambda x: (x[0] - target[0])**2 + (target[1] - x[1])**2)
        danger = ghosts[0]
        print(danger)
        escape = abs(target[0]) + abs(target[1])
        no_escape = (max(target[0],danger[0]) - min(target[0],danger[0])) + (max(target[1],danger[1]) - min(target[1],danger[1]))
        print(escape,no_escape)
        return escape<no_escape
        