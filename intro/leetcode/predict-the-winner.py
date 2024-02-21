class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def helper(start, end):

            if start > end:
                return 0
            
            starting, ending = nums[start], nums[end]
            left, right = helper(start + 1, end), helper(start, end - 1)

            return max(starting - left, ending - right)
        
        return helper(0, len(nums) - 1) >= 0
            

