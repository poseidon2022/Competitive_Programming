# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        greater = ListNode()
        dummy = ListNode()
        wan = greater
        ans = dummy
        s = head
        while s:
            if s.val < x:
                dummy.next = ListNode(s.val)
                dummy = dummy.next
            s = s.next
        
        while head:
            if head.val >= x:
                greater.next = ListNode(head.val)
                greater = greater.next

            head = head.next
        
        dummy.next = wan.next
        return ans.next

        


        