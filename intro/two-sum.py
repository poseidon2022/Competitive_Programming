class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mine = defaultdict(list)
        for idx, val in enumerate(nums): mine[val].append(idx)

        nums.sort()
        i, j = 0, len(nums)-1
        while i!=j:
            if nums[i]+nums[j]<target: i+=1
            elif nums[i] + nums[j]> target: j-=1
            elif nums[i]==nums[j]: return [mine[nums[i]][0], mine[nums[i]][-1]]
            else: return [mine[nums[i]][0], mine[nums[j]][0]]

        