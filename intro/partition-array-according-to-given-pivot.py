class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equals = []
        greater = []
        for i in nums:
            if i<pivot: less.append(i)
            elif i==pivot: equals.append(i)
            else: greater.append(i)
        equals.pop()

        return less + equals + [pivot] + greater
        