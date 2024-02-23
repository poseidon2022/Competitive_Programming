# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        self.ans = float('inf')
        def helper(root):

            if not root:
                return
            
            if root.val==p.val or root.val==q.val:
                self.ans = root.val
                return

            if (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
                self.ans = root.val
                return
                        
            

            if (p.val < root.val and q.val < root.val): return helper(root.left)
            
            return helper(root.right)
        

        helper(root)
        return TreeNode(self.ans)
            

            

                
            
            
