class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mine = defaultdict(int)
        tracker = defaultdict(int)
        bef = defaultdict(int)
        count = Counter(nums)

        ans = []
        for i in range(len(nums)): mine[nums[i]]+=i

        for i in range(len(nums)):
            o = abs(bef[nums[i]] - tracker[nums[i]] * i)
            tracker[nums[i]]+=1
            mine[nums[i]] -= i
            n = abs((count[nums[i]] - tracker[nums[i]])*i - (mine[nums[i]]))
            bef[nums[i]]+=i
            ans.append(o + n)

        return ans

        