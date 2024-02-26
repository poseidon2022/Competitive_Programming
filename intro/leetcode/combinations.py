class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        def helper(arr, cur):
            if len(arr) == k:
                ans.append(arr[:])
                return
            if cur > n:
                return
            

            arr.append(cur)
            helper(arr, cur + 1)
            arr.pop()
            helper(arr, cur + 1)
        
        helper([],1)
        return ans
            