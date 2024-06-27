# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        total_count = (n * (n - 1)) // 2
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def helper(node):
            queue = deque([node])
            count = 1
            while queue:
                cur = queue.popleft()
                for vertex in graph[cur]:
                    if vertex not in visited:
                        count += 1
                        queue.append(vertex)
                        visited.add(vertex)
            return count
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                count = helper(node)
                total_count -= (count * (count - 1)) // 2
        
        return total_count


        
        


