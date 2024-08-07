# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        low = 0
        high = len(arr) - 1
        ref = float('inf')
        while low <= high:

            mid = (low + high) // 2
            if abs(arr[mid] - x) < ref:
                ref =  abs(arr[mid] - x)
                temp = mid
            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else: break

                
        
        ans = []
        
        print(mid)
        low = temp - 1
        high = temp
        while len(ans) < k:
            if low < 0:
                while len(ans) < k:
                    ans.append(arr[high])
                    high += 1
                break
            elif high >= len(arr):
                while len(ans) < k:
                    ans.append(arr[low])
                    low -= 1
                break

            if abs(arr[low] - x) <= abs(arr[high] - x):
                ans.append(arr[low])
                low -= 1
            else:
                ans.append(arr[high])
                high += 1
            
        return sorted(ans)
