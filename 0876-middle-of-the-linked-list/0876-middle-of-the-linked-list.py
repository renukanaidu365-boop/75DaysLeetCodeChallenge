# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        length=0
        while t:
            length=length+1
            t=t.next
        mid=length//2
        t=head
        for _ in range(mid):
            t=t.next
        return t



