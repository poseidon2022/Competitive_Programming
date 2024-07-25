# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        mine = defaultdict()
        for idx, num in enumerate(nums):
            num = str(num)
            formed = ''
            for digit in num:
                formed += str(mapping[int(digit)])
            
            mine[int(num)] = (int(formed), idx)
        

        nums.sort(key = lambda x: mine[x])
        return nums

        