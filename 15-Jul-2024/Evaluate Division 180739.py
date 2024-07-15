# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mine = defaultdict(list)
        ans = []

        for (a, b), val in zip(equations, values):
            mine[a].append((b, val))
            mine[b].append((a, 1 / val))

        def helper(mine, visited, num, denom, query):
            if num not in mine or query[1] not in mine:
                return -1.0
            if num == query[1]:
                return denom

            visited.add(num)
            for nxt, val in mine[num]:
                if nxt not in visited:
                    res = helper(mine, visited, nxt, denom * val, query)
                    if res != -1.0:
                        return res
            visited.remove(num)

            return -1.0

        for query in queries:
            ans.append(helper(mine, set(), query[0], 1.0, query))

        return [-1.0 if x == -1.0 else round(x, 5) for x in ans]