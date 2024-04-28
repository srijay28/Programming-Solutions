# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(None)
        dum.next = head
        curr,prev = head,dum
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dum.next

        