class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mine = defaultdict(int)
        for i in nums:
            mine[i]+=1
        
        ans = 1
        nums.sort()
        if not nums: return 0
        for i in nums:
            val = 0
            while mine[i]>0:
                mine[i]-=1
                i+=1
                val+=1
            ans = max(ans,val)
        
        return ans



        