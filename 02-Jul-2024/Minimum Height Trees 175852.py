# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(set)
        if n==1 or not edges: return [0]
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        ans = []
        for node in graph:
            if len(graph[node]) == 1:
                ans.append(node)

        while n > 2:

            n -= len(ans)
            next_iter = []
            for cur in ans:
                for node in graph[cur]:
                    graph[node].remove(cur)
                    if len(graph[node]) == 1:
                        next_iter.append(node)
            
            ans = next_iter
        
        return ans
        
        

