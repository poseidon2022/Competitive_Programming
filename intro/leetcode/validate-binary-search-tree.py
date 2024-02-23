# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = list()
        def helper(root,_min,_max):
            if not root: return True


            if root.val>=_min:
                return False
            if root.val<=_max:
                return False

            return helper(root.left,root.val,_max)==True and helper(root.right,_min,root.val)==True
            
        return helper(root,float('inf'),float('-inf'))
        