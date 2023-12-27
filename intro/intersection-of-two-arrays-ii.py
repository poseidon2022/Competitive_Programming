class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        nums1.sort()
        ans = []
        i,j = 0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                ans.append(nums2[j])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]: j+=1
            elif nums1[i]<nums2[j]: i+=1
        
        return ans

        