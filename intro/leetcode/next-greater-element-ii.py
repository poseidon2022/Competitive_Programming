class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]
        n = len(nums)
        nums.extend(nums)
        sta = []
        for i in range(len(nums)):
            while sta and nums[i] > sta[-1][1]:
                idx = sta[-1][0]
                if idx < n:
                    ans[idx] = nums[i]
                sta.pop()
            sta.append((i, nums[i]))
        
        return ans

        