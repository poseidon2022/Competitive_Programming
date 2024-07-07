# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #[2,3,4,5]
        #[0,1,5,10,11,14]
        #[0,1,1,4,5,6,6,6]
        #[20,75,81,82,95]

        nums.sort()
        if len(nums)<=4:
            return 0
        return min(nums[-4]-nums[0], nums[-1]-nums[3], nums[-2] - nums[2], nums[-3] - nums[1])