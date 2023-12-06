class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i,j = 0,n
        shuffled = []
        while j<len(nums):
            shuffled.extend([nums[i], nums[j]])
            i+=1
            j+=1
        return shuffled
        