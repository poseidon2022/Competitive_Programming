# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.ans = float('-inf')
        def helper(root, _max, _min):
            if not root:
                a = abs(_min - _max)
                self.ans = max(self.ans, a)
                return

            _min = min(root.val, _min)
            _max = max(root.val, _max)
            helper(root.left, _max, _min)
            helper(root.right, _max, _min)

        helper(root, float('-inf'), float('inf'))
        return self.ans
        