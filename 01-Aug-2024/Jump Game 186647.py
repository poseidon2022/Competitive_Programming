# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _max = nums[0]
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if _max==0: return False
            _max = max(_max - 1, nums[i])
        
        return True
            



        