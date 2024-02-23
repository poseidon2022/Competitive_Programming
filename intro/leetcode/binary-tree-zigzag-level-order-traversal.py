# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []
        arr = [] 
        queue = deque([(root, 0)])
        prev = 0
        f = True
        while queue:
            if not f and prev != queue[0][1]:
                f = not f
                prev = queue[0][1]
                ans.append(arr)
                arr = []

            elif f and prev != queue[-1][1]:
                f = not f
                prev = queue[-1][1]
                ans.append(arr)
                arr = []
            
            curNode, level = queue.popleft() if (not f) else queue.pop()
            if curNode:
                if not f:
                    queue.append((curNode.right, level + 1))
                    queue.append((curNode.left, level + 1))
                else:
                    queue.appendleft((curNode.left, level + 1))
                    queue.appendleft((curNode.right, level + 1))
                
                arr.append(curNode.val)
            
        if arr: ans.append(arr)
        return ans



            


        
        