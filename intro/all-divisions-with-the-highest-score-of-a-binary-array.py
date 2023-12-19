class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        mine = defaultdict(int)
        anot = defaultdict(list)
        mine[0] = 0
        mine[1] = nums.count(1)
        for idx, val in enumerate(nums):
            _sum = mine[1] + mine[0]
            anot[_sum].append(idx)
            if val==0: mine[0]+=1
            if val==1: mine[1]-=1

        _sum = mine[1] + mine[0]
        anot[_sum].append(idx+1)
        temp = max(anot.keys())
        return anot[temp]

