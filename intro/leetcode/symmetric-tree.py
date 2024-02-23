# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        mine = defaultdict(list)
        def helper(root, l):
            if not root:
                mine[l].append(None)
                return
            
            mine[l].append(root.val)
            helper(root.left, l + 1)
            helper(root.right, l + 1)
        
        helper(root, 0)
        for i in mine:
            left = mine[i][:len(mine[i])//2]
            right = mine[i][len(mine[i])//2:][::-1]
            if left != right and len(mine[i])!=1:
                return False
        
        return True

        