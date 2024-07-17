# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n, m = len(targetGrid), len(targetGrid[0])
        colors = defaultdict(list)
        for row in range(n):
            for col in range(m):
                colors[targetGrid[row][col]].append([row,col])
            
        graph, indegree = defaultdict(list), defaultdict(int)
        for c1 in colors:
            x1, x2 = min([item[0] for item in colors[c1]]), max([item[0] for item in colors[c1]])
            y1, y2 = min([item[1] for item in colors[c1]]), max([item[1] for item in colors[c1]])
            for c2 in colors:
                if c1 != c2:
                    for x, y in colors[c2]:
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            graph[c1].append(c2)
                            indegree[c2] += 1
                            break
        

        queue = deque([node for node in colors if indegree[node] == 0])
        while queue:
            cur = queue.popleft()
            for node in graph[cur]:
                indegree[node] -= 1
                if not indegree[node]:
                    queue.append(node)
        
        return all(indegree[node] == 0 for node in indegree)
        
        