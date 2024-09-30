# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.ans = True
        def helper(root, level):

            if not root: return level

            left = helper(root.left, level + 1)
            right = helper(root.right, level + 1)
            if abs(left - right) > 1: self.ans = False

            return max(left, right)
        
        helper(root, 0)
        return self.ans
            

            


        