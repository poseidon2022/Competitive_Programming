# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ans = head
        head2 = head
        while head2:
            if head2.val!=head.val:
                head.next = head2
                head = head.next
            head2 = head2.next
        if head: head.next = None      
        return ans
        



        