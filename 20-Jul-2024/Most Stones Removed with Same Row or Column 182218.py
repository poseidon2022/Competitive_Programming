# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        #starting from each node, try to construct the union dict by row or column
        #try to compare the dictionaries and decide on the max removal you took
        #row_parent and col_parent
        #stones on each connected component - 1

    
        sameRow = defaultdict(list)
        sameCol = defaultdict(list)
        for row,col in stones:
            sameRow[row].append([row, col])
            sameCol[col].append([row, col])
        
        visited = set()
        count = 0
        for row, col in stones:
            if (row, col) not in visited:
                queue = deque([(row,col)])
                visited.add((row,col))
                while queue:
                    curRow, curCol = queue.popleft()
                    for r,c in sameRow[curRow]:
                        if (r,c) not in visited:
                            count += 1
                            queue.append((r, c))
                            visited.add((r,c))

                    for r,c in sameCol[curCol]:
                        if (r,c) not in visited:
                            count += 1
                            queue.append((r, c))
                            visited.add((r,c))
        return count


        
        


        