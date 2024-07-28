# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def helper(nums,k):

            mine = defaultdict(int)
            l, ans = 0, 0
            for r in range(len(nums)):
                mine[nums[r]] += 1
                while len(mine) > k:
                    mine[nums[l]] -= 1
                    if not mine[nums[l]]:
                        del mine[nums[l]]
                    l += 1
                
                ans += (r - l + 1)
            return ans
            
        return helper(nums,k) - helper(nums,k-1)
                    

        



        