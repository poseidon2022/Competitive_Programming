# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = []
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            ans.append(root.val)
            helper(root.right)
        
        helper(root)
        return all(ans[i] > ans[i-1] for i in range(1, len(ans)))

        
        