# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        self.ans = False

        def helper(root, head):
            if not head:
                return True
            if not root:
                return False

            if root.val == head.val:
                if helper(root.left, head.next) or helper(root.right, head.next):
                    return True
            return False

        def traverseTree(root, head):
            if not root:
                return False
            if helper(root, head):
                return True
            return traverseTree(root.left, head) or traverseTree(root.right, head)

        return traverseTree(root, head)
