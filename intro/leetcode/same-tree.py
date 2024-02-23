# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = list()
        def same(root):
            if not root:
                ans.append(None)
                return

            ans.append(root.val)
            same(root.left)
            same(root.right)
        same(p)
        same(q)
        n = len(ans)
        return ans[:n//2] == ans[n//2:]