class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        ans = 0
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            anot = nums[i]
            while j<k:
                fin = anot + nums[j] + nums[k]
                if fin < target: j+=1
                elif fin > target: k-=1
                else: return fin
                if abs(target - fin) < diff:
                    ans = fin
                    diff = abs(target - fin)
        
        return ans



         