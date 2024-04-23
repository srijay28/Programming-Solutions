# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(ini,final):
            prev = None
            curr = ini
            while(curr != final):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        n = 1
        curr = head
        last = prev = None
        
        while True and curr:
            l = 0
            initial = curr #initial of the current group
            prev = last #last of the previous group to be connected to
            
            while (l < n) and curr:
                last = curr
                curr = curr.next
                l += 1
            
            if l % 2 == 0:  #reverse the nodes: reverse(initial,curr) curr is the first of the coming group which should be connected to ini after reversal
                
                rev = reverse(initial,curr)
                prev.next = rev
                initial.next = curr
                last = initial
            
            n += 1
        return head

            

                
