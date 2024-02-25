# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        mine = defaultdict(int)
        def helper(root):
            if not root:
                return

            mine[root.val] += 1
            helper(root.left)
            helper(root.right)
        

        helper(root)
        wan = list(mine.items())
        wan.sort(key = lambda x: x[1], reverse = True)
        ans = []
        ref = wan[0][1]
        for key, val in wan:
            if val == ref:
                ans.append(key)
            else: break
        
        return ans

