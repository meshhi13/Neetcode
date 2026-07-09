# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseKGroupRec(head):
            nonlocal k
            if not head:
                return None

            s = []

            copy = head

            count = 0

            for i in range(k):
                s.append(copy)
                if copy:
                    copy = copy.next
                else:
                    return head

            newCopy = ListNode(0)
            linkedlist = newCopy

            for i in s[::-1]:
                newCopy.next = i
                newCopy = newCopy.next

            newCopy.next = reverseKGroupRec(copy)

            return linkedlist.next

        resNode = ListNode(0, head)

        resNode.next = reverseKGroupRec(head)

        return resNode.next
