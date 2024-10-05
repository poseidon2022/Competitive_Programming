# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        magic_number = max(nums)
        ans = 0
        temp = 0
        for idx in range(len(nums)):
            if nums[idx] == magic_number: temp += 1
            else: temp = 0
            ans = max(ans, temp)
            
        return ans    