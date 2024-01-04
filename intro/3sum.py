class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for k in range(len(nums) - 2):
            i,j = k+1, len(nums)-1
            tar = -nums[k] 
            mine = []
            while i<j:
                if nums[i] + nums[j] < tar: i+=1
                elif nums[i] + nums[j] > tar: j-=1
                else:
                    mine = [-tar, nums[i], nums[j]]
                    ans.add(tuple(mine))
                    i+=1
                    j-=1
        final = list(map(list, ans))
        return final