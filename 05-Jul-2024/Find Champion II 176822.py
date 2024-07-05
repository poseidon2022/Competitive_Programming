# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        ans = []
        print(graph)
        for i in range(n):
            queue = deque([i])
            inter = []
            visited = {i}
            while queue:
                cur = queue.popleft()
                for node in graph[cur]:
                    if node not in visited:
                        inter.append(node)
                        queue.append(node)
                        visited.add(node)
            
            if len(inter)==n - 1:
                ans.append(i)
        
        print(ans)
        return ans[0] if len(ans) == 1 else -1
        