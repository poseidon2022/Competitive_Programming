t = int(input())
from collections import defaultdict

for _ in range(t):

    n = int(input())
    instn = input()
    mine = defaultdict(list)
    ans = float('inf')
    for i in range(n):
        l,r = map(int, input().split())
        mine[i].append(l - 1)
        mine[i].append(r - 1)


    ans = float('inf')
    stack = [(0,0)]
    while stack:
        node, count = stack.pop()
        if all(i == -1 for i in mine[node]):
            ans = min(ans, count)
            continue
        
        elif instn[node] == 'U':
            for i in mine[node]:
                if i != -1:
                    stack.append((i, count + 1))
        
        elif instn[node] == 'L':
            for i in range(len(mine[node])):
                if i == 1 and mine[node][i]!=-1:
                    stack.append((mine[node][i], count + 1))
                elif mine[node][i] != -1:
                    stack.append((mine[node][i], count))
        
        elif instn[node] == 'R':
            for i in range(len(mine[node])):
                if i == 0 and mine[node][i]!=-1:
                    stack.append((mine[node][i], count + 1))
                elif mine[node][i] != -1:
                    stack.append((mine[node][i], count))
    print(ans)


