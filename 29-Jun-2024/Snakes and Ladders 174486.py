# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        mine = defaultdict(tuple)
        numbers = defaultdict(int)
        r = True
        count = 1
        for i in range(len(board)-1, -1, -1):
            sta = 0 if r else len(board) - 1
            fac = 1 if r else -1
            for j in range(len(board)):
                mine[count] = (i, sta)
                numbers[(i, sta)] = count
                sta += fac
                count += 1
            r = not r
    

        n = len(board)
        queue = deque([(1,0)])
        visited = {1}

        while queue:
            cur,cnt = queue.popleft()
            for i in range(1, 7):
                node = cur + i
                row, col =  mine[node]
                if board[row][col] != -1:
                    node = board[row][col]
                if node == n*n:
                    return cnt + 1
                if node not in visited:
                    queue.append((node, cnt + 1))
                    visited.add(node)


        return -1


        

