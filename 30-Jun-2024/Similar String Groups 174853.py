# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        #I think the letters make the nodes
        #difference should be len(word_in_strs) - 2
        #we can use union find to find the connected components

        def similar(word1, word2):
            count = 0
            for k in range(len(word1)):
                if word1[k] != word2[k]:
                    count += 1
            
            return count <= 2

        ans = 0
        visited = set()
        for i in range(len(strs)):
            if strs[i] not in visited:
                ans += 1
                queue = deque([strs[i]])
                visited.add(strs[i])
                while queue:
                    cur = queue.popleft()
                    for j in range(i+1, len(strs)):
                        if strs[j] not in visited and similar(cur, strs[j]):
                            queue.append(strs[j])
                            visited.add(strs[j])
        
        return ans


                    
