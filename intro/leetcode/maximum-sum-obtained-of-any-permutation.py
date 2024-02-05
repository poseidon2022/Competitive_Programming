class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        inter = [0 for _ in range(len(nums))]
        for sta, end in requests:
            inter[sta]+=1
            if end + 1< len(nums): inter[end+1]-=1
        
        pref = [0 for _ in range(len(nums))]
        pref[0] = inter[0]
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + inter[i]

        nums.sort()
        pref.sort(reverse = True)
        ans = 0
        for i in range(len(pref)):
            k = nums.pop()
            ans += k*pref[i]
        return ans % (10**9 + 7)