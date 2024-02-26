class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def helper(cur, arr):
            ans.append(arr[:])
            if len(arr) == len(nums):
                return
            
            for i in range(cur, len(nums)):
                arr.append(nums[i])
                helper(i + 1, arr)
                arr.pop()
        
        helper(0, [])
        return ans


        