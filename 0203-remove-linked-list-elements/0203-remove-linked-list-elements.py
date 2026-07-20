# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        c=head 
        while head and head.val==val:
            head=head.next
        while c.next and c:
            if c.next.val==val:
                c.next=c.next.next
            else:
                c=c.next
        return head