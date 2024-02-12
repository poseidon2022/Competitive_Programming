# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or head.next==None:
            return head
        ans = head
        e = head.next
        fin = e
        while head and head.next and head.next.next:
            head.next = head.next.next
            if e and e.next:
                e.next = e.next.next
                e = e.next
            head = head.next

        if head: head.next = fin

        return ans

        
        
        