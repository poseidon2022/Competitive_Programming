# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        root = TreeNode()        
        def helper(arr, root):

            if not arr:
                return 

            max_index = arr.index(max(arr))
            wanted = arr[max_index]
            root = TreeNode(wanted)
            root.left = helper(arr[:max_index], root.left)
            root.right = helper(arr[max_index + 1:], root.right)

            return root
        
        return helper(nums, root)


        