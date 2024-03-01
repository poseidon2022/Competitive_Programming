# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        level_min = defaultdict(lambda: float('inf'))
        level_max = defaultdict(lambda: 0)

        def helper(root, l_shift, r_shift, level):
            if not root:
                return
            
            level_min[level] = min(level_min[level], r_shift)
            level_max[level] = max(level_max[level], 2**level - l_shift)

            helper(root.left, 2 * l_shift + 1, 2 * r_shift, level + 1)
            helper(root.right, 2 * l_shift, 2 * r_shift + 1, level + 1)
        
        helper(root,0, 0, 0)
        ans = 0
        for i in level_min:
            ans = max(ans, level_max[i] - level_min[i])
        return ans





        