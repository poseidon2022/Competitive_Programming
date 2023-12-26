class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        _max = max(arr1)
        counter = [0 for _ in range(_max + 1)]
        for i in arr1: counter[i]+=1
        ans = []
        print(counter)
        for i in arr2:
            ans.extend([i]*counter[i])
            counter[i] = -1
        
        for idx, val in enumerate(counter):
            if val!=0 and val!=-1: ans.extend([idx]*val)
 
        return ans

        

        