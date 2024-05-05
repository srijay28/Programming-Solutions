# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        stack = []
        while curr:
            temp = curr.next
            curr.next = None
            if not stack:
                stack.append(curr)
            else:
                while stack and stack[-1].val < curr.val:
                    stack.pop()
                stack.append(curr)
            curr = temp
        
        for i in range(len(stack)):
            if i == len(stack) - 1:
                stack[i].next = None
                break
            stack[i].next = stack[i+1]
        return stack[0]
            
