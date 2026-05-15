# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = []
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        slow = temp

        while slow:
            s.append(slow)
            slow = slow.next
        
        curr = head
        for i in s[::-1]:
            print(i.val)
            i.next = curr.next
            curr.next = i
            curr = curr.next.next
        



        