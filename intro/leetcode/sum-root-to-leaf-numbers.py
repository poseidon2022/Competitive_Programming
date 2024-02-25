# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        def helper(root, s):
        
            if not root:
                return

            if not root.right and not root.left:
                s += str(root.val)
                self.ans += int(s)
                return
            
            helper(root.left, s + str(root.val))
            helper(root.right, s + str(root.val))
        
        helper(root, '')
        return self.ans


        