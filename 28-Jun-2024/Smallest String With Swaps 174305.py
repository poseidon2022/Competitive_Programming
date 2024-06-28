# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # parent = {i:i for i in range(len(s))}
        # def find(node):
        #     if parent[node] == node:
        #         return node
            
        #     parent[node] = find(parent[node])
        #     return parent[node]
    

        # def union(node1, node2):
        #     parent1 = parent[node1]
        #     parent2 = parent[node2]
        #     if parent1 != parent2:
        #         if s[parent1] < s[parent2]:
        #             parent[parent2] = parent1
        #         else:
        #             parent[parent1] = parent2
        
        # for a, b in pairs:
        #     union(parent[a], parent[b])
        
        # print(parent)
        # return ""

        graph = defaultdict(list)
        for a,b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def helper(node):

            queue = deque([node])
            visited.add(node)
            final = [node]
            while queue:
                cur = queue.popleft()
                for vert in graph[cur]:
                    if vert not in visited:
                        queue.append(vert)
                        visited.add(vert)
                        final.append(vert)
            return final
    
        ans = [' ' for _ in range(len(s))]
        for node in range(len(s)):

            if node not in visited:
                ret = helper(node)
                ret.sort()
                form = {i:ret[i] for i in range(len(ret))}
                ret.sort(key = lambda x: s[x])
                for idx in range(len(ret)):
                    ans[form[idx]] = s[ret[idx]]
        
        return ''.join(ans)



                    




        