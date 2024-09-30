# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = deque()
        if not root:
            return
        stack.appendleft(root.val)
        def helper(root):
            if not root:
                return
            while root:
                k = root.pop()
                stack.appendleft(k.val)
                helper(k.children)
            
        
        helper(root.children)
        return stack 
            

            

    
        return []

        