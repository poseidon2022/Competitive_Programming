# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        mine = defaultdict(list)
        def helper(root, c, r):

            if not root:
                return
            
            mine[(c, r)].append(root.val)
            helper(root.left, c - 1, r + 1)
            helper(root.right, c + 1, r + 1)
        
        helper(root, 0, 0)
        ans = []
        
        anot = defaultdict(list)
        bef_all = []
        for i in mine:
            bef_all.append(i)
        bef_all.sort()
        for i in bef_all:
            anot[i[0]].extend(sorted(mine[i]))
        inter = []
        for i in anot:
            inter.append(i)
        final = []
        inter.sort()
        for i in inter:
            final.append(anot[i])
        
        return final

        

        