class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            d = nums[i] > 0
            r = i
            prev = r
            f = 0
            mine = defaultdict(int)
            while mine[r] < 1:

                r = r%len(nums)
                c = nums[r] > 0
                if c!=d or (f>0 and prev==r): break
                mine[r]+=1
                if mine[r]==2: return True
                prev = r
                r+=nums[r]
                f+=1
        
        return False

        