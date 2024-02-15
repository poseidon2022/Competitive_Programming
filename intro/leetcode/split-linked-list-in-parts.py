# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        ans = []
        count = 0
        dummy = head
        while head:
            count += 1
            head = head.next

        parts = count//k
        rem = count%k
        while dummy:
            new = ListNode()
            wan = new
            c = 0
            while c < parts:
                
                new.next = dummy
                dummy = dummy.next
                new.next.next = None
                new = new.next
                c += 1

            if rem:
                
                new.next = dummy
                dummy = dummy.next
                new.next.next = None
                rem -= 1

            ans.append(wan.next)
        
        while len(ans) < k: 
            ans.append(ListNode().next)
        return ans

                


        

        