class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        _min = 1
        ans = []
        for i in range(len(arr)-1,-1,-1):
            print(arr, i)
            idx = arr[:i+1].index(_min)
            
            arr[:idx+1] = arr[:idx+1][::-1]
            arr[:i+1] = arr[:i+1][::-1]
            ans.append(idx + 1)
            ans.append(i + 1)
            _min += 1
        
        ans.append(len(arr))
        return ans
