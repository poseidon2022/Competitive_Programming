# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        ans = final
        cur = 0
        head = head.next
        while head:
            if head.val==0:
                final.next = ListNode(cur)
                final = final.next
                cur = 0

            cur+=head.val
            head = head.next
            
        
        return ans.next
        
        