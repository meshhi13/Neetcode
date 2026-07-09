# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        s = []

        copy = head

        count = 0

        while copy:
            s.append(copy)
            copy = copy.next

        newCopy = ListNode(0)
        linkedlist = newCopy

        for i in s[::-1]:
            newCopy.next = i
            newCopy = newCopy.next

        newCopy.next = None

        return linkedlist.next

            