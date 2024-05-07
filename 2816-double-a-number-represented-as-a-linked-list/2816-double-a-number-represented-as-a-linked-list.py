# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0)
        prev = dum
        curr = head
        temp = 0
        while curr != None:
            temp = curr.val*2
            curr1 = ListNode(0)
            if temp > 9:
                prev.val += temp // 10
            curr1.val = temp % 10
            prev.next = curr1
            prev = curr1
            curr = curr.next
        if dum.val == 0:
            return dum.next
        return dum

