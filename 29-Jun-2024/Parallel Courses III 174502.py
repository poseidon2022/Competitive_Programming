# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:


        indegree = [0 for _ in range(n)]
        final = defaultdict(int)
        graph = defaultdict(list)
        for a,b in relations:
            indegree[b-1] += 1
            graph[a - 1].append(b - 1)
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                final[i] = time[i]
                queue.append(i)


        while queue:
            cur = queue.popleft()
            for node in graph[cur]:
                indegree[node] -= 1
                final[node] = max(final[node], final[cur] + time[node])
                if indegree[node] == 0:
                    queue.append(node)
            
        
        return max(final.values())

        


        