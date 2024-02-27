class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        mine = set()
        def helper(cur, arr):
            mine.add(tuple(sorted(arr[:])))
            if len(arr) == len(nums):
                return
            

            for i in range(cur, len(nums)):
                arr.append(nums[i])
                helper(i + 1, arr)
                arr.pop()
        
    
        helper(0, [])
        ans = list(map(list, mine))
        return ans