# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def maximumSum(root, _sum, isBST, maxLeft, minRight):

            if not root:
                return [_sum, True, maxLeft, minRight]
            
            if not root.right and not root.left:
                self.ans = max(self.ans, root.val)
                return [root.val, True, max(root.val, maxLeft), min(root.val, minRight)]
            

            left_sum, isBST_left, maxL, minL = maximumSum(root.left, 0, True, maxLeft, minRight)
            right_sum, isBST, maxR, minR = maximumSum(root.right, 0, True, maxLeft, minRight)
            all_sum  = left_sum + right_sum + root.val
            if (isBST and isBST_left) and maxL < root.val < minR:
                self.ans = max(self.ans, all_sum)
                return [all_sum, True, max(root.val, maxL, maxR), min(root.val, minR, minL)]
            else:
                return [all_sum, False, maxLeft, minRight]
        
        maximumSum(root,0, True, float('-inf'), float('inf'))
        return self.ans