# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.ans = 0
        def helper(root):
            if not root:
                return
            
            value = root.val
            if low < value < high:
                self.ans += value
                helper(root.left)
                helper(root.right)
            if value >= high:
                if value ==  high:
                    self.ans += value

                helper(root.left)
            if value <= low:
                if value == low:
                    self.ans += value
                helper(root.right)
    
        helper(root)
        return self.ans
                