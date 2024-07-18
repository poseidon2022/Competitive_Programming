# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        self.ans = 0
        def helper(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_distance = helper(node.left)
            right_distance = helper(node.right)
            for l_h in left_distance:
                for r_h in right_distance:
                    if l_h + r_h <= distance:
                        self.ans += 1
            
            new_height = []
            for h in left_distance + right_distance:
                if h < distance:
                    new_height.append(h + 1)
            
            return new_height

        helper(root)
        return self.ans
            
        