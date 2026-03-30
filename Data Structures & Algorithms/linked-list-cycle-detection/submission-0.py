# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        nex = head.next

        while nex:
            if nex == cur:
                return True

            nex = nex.next
            if nex:
                nex = nex.next
            cur = cur.next

        return False