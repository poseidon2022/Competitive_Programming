class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        pref = []
        ans = 0
        for i in range(len(matrix)):
            wan = matrix[i]
            pref.append(list(accumulate(wan)))

        for i in range(len(pref[0])):
            for j in range(i, len(pref[0])):
                mine = defaultdict(int)
                mine[0] = 1
                cur = 0
                for r in range(len(pref)):
                    cur += pref[r][j] if i==0 else pref[r][j] - pref[r][i - 1]
                    ans += mine[cur - target]
                    mine[cur] += 1
        
        return ans




                
        