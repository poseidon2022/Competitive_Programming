# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        self.s = []
        self.e = []
        def helper(node, path):
    
            if not node or (self.s and self.e):
                return
            if node.val == startValue:
                self.s = path[:]
            if node.val == destValue:
                self.e = path[:]

            path.append("L")
            left = helper(node.left, path)
            path.pop()
            path.append("R")
            right = helper(node.right,path)
            path.pop()

            return 

        helper(root,[])
        staPtr, endPtr = 0, 0
        while staPtr < len(self.s) and endPtr < len(self.e):
            if self.s[staPtr] != self.e[endPtr]:
                break
            staPtr += 1
            endPtr += 1

        return 'U'*(len(self.s) - staPtr) + ''.join(self.e[endPtr:])
        
            
    