class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def helper(arr, visited):

            if len(arr) == len(nums):
                ans.append(arr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    arr.append(nums[i])
                    visited.add(nums[i])
                    helper(arr, visited)
                    visited.remove(nums[i])
                    arr.pop()
            
        helper([], set())
        return ans
        