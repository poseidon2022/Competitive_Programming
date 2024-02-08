class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mine = defaultdict(int)
        cur = 0
        ans = 0
        mine[0] = 1
        for i in range(len(nums)):
            cur+=nums[i]
            tar = cur%k
            ans+=mine[tar]
            mine[tar]+=1

        return ans


            

        
        

        
        