class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        def helper(arr, cur):
            if len(arr) == k:
                ans.append(arr[:])
                return
            
            if n - cur + 1 < k - len(arr):
                return
            
            for i in range(cur, n+1):

                arr.append(i)
                helper(arr, i + 1)
                arr.pop()
        
        helper([],1)
        return ans
            