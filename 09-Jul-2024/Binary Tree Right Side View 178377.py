# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque([root])
        print(queue)
        temp = None
        while queue:
            n = len(queue)
            for i in range(n):
                k = queue.popleft()
                if k!=None:
                    queue.append(k.left)
                    queue.append(k.right)
                    temp = k.val
            if temp!=None: ans.append(temp)
            temp = None
        
        return ans
        