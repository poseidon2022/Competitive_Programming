# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def helper(root, key):
            
            if not root or (root and root.val == key):
                return root
            
            if root.val > key:
                return helper(root.left, key)
            return helper(root.right, key)
        
        return helper(root, val)
        