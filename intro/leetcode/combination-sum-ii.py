class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        candidates.sort()
        def helper(arr, cur, _sum):
            if _sum >= target:
                if _sum == target:
                    ans.append(arr[:])
                return
            visited = set()
            for i in range(cur, len(candidates)):
                if candidates[i] not in visited:
                    arr.append(candidates[i])
                    helper(arr, i + 1, _sum + candidates[i])
                    arr.pop()
                    visited.add(candidates[i])
            
        helper([],0,0)
        return ans