# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = 0

        graph = []
        for i in range(len(points)):
            for j in range(i + 1,len(points)):
                
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                graph.append((weight, i, j))

        graph.sort()
        unionFind = UnionFind(len(points))

        nodes = 0
        for node in graph:
            if unionFind.union(node[1], node[2]):
                min_cost += node[0]
                nodes += 1
            if nodes == len(points) -1:
                break

        return min_cost

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.groups = size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.groups -= 1
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        else:
            return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)