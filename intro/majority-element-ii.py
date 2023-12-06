class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        target = len(nums)//3
        majority = []
        counter = defaultdict(int)
        for i in nums:
            counter[i]+=1
        
        for i in counter:
            if counter[i]>target: majority.append(i)
        
        return majority
        