t = int(input())
from collections import defaultdict
for i in range(t):
    n = int(input())
    mine = defaultdict(int)
    arr = list(map(int, input()))
    nums = []
    for i in arr:
        nums.append(i - 1)
    
    cur = 0
    ans = 0
    mine[0] = 1
    for i in range(len(nums)):
        cur+=nums[i]
        ans += mine[cur]
        mine[cur]+=1

    
    
    print(ans)