class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []
        def helper(arr, cur, _sum):
            if len(arr) == k:
                if _sum == n:
                    ans.append(arr[:])
                return
            
            for i in range(cur, 10):
                arr.append(i)
                helper(arr, i + 1, _sum + i)
                arr.pop()
            
        helper([], 1, 0)
        return ans


        