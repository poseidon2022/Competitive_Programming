class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mine = defaultdict(int)
        dict2 = defaultdict(int)
        anot = sorted(nums)
        for i in range(len(nums)):
            dict2[anot[i]] = i - mine[anot[i]]
            mine[anot[i]]+=1
        
        for idx,val in enumerate(nums):
            nums[idx] = dict2[val]
        
        return nums
            