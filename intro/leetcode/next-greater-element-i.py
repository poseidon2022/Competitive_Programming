class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mine = defaultdict(lambda: -1)
        sta = []
        for num in nums2:
            while sta and sta[-1] < num:
                mine[sta[-1]] = num
                sta.pop()
            
            sta.append(num)
        
        return [mine[num] for num in nums1]
        