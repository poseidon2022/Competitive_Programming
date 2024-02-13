# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(float('-inf'))
        dummy.next = head
        kept = dummy
        dummy = dummy.next
        while dummy:
            now = dummy.val
            wanted = kept
            f = False
            while wanted and wanted.next:
                if wanted.next == dummy:
                    if f: wanted.next = wanted.next.next
                    break
                if not f and wanted.next.val > now:
                    f = True
                    nxt = wanted.next
                    inserted = ListNode(now)
                    wanted.next = inserted
                    inserted.next = nxt
                    wanted = nxt
                    continue
                
                
                wanted = wanted.next
            
            dummy = dummy.next

        
        return kept.next



        