class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def helper(arr):
            _sum = sum(arr)
            if _sum >= target:
                if _sum == target:
                    ans.add(tuple(sorted(arr[:])))
                
                return
            
            for i in range(len(candidates)):
                arr.append(candidates[i])
                helper(arr)
                arr.pop()
        
        helper([])
        final = list(map(list, ans))
        return final

