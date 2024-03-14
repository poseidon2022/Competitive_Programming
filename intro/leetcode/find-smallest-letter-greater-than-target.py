class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        sta = 0
        end = len(letters) - 1
        while sta <= end:

            mid = (sta + end) // 2
            if letters[mid] > target:
                end = mid - 1
            else:
                sta = mid + 1
        
        return letters[end + 1] if end < len(letters) - 1 else letters[0]
        
        