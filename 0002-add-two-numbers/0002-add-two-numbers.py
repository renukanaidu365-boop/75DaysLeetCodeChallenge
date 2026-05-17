# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode()
        c=d
        ca=0
        while l1 or l2 or ca:
            v1=l1.val if l1 else 0
            
            v2=l2.val if l2 else 0
            t=v1+v2+ca
            ca=t//10
            c.next=ListNode(t%10)
            c=c.next
            if l1: l1=l1.next
            if l2: l2=l2.next
        return d.next        
        