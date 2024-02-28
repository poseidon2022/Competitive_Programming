# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        root = TreeNode(nums[n//2])
        ans = root
        left = nums[:n//2]
        right = nums[n//2 + 1:]
        def helper(root, lar, sma):

            if len(lar)==0 and len(sma)==0:
                return
            
            if len(sma)!=0:
                s = len(sma)
                root.left = TreeNode(sma[s//2])
                helper(root.left,sma[s//2 + 1:], sma[:s//2])

            if len(lar)!=0:
                l = len(lar)
                root.right = TreeNode(lar[l//2])
                helper(root.right,lar[l//2 + 1:],lar[:l//2])
        
        helper(root,right, left)
        return ans
            

            

        
        return ans



        