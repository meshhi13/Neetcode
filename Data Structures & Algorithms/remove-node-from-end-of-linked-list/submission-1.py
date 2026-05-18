# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sid = 0
        curr = head
        while curr:
            sid += 1
            curr = curr.next

        new_head = ListNode(next=head)
        curr = new_head
        for i in range(sid - n):
            curr = curr.next

        curr.next = curr.next.next

        return new_head.next