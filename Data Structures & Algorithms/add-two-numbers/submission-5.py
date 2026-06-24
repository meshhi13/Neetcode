# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False 
        ret = ListNode()
        head = ret
        prev = ListNode()
        while l1 and l2:
            sumQ = l1.val + l2.val + (1 if carry else 0)
            if sumQ >= 10:
                sumQ -= 10
                carry = True
            else:
                carry = False
            ret.val = sumQ
            prev = ret
            if l1.next or l2.next:
                ret.next = ListNode()
                ret = ret.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sumQ = l1.val + (1 if carry else 0)
            if sumQ >= 10:
                sumQ -= 10
                carry = True
            else:
                carry = False
            ret.val = sumQ
            prev = ret
            if l1.next:
                ret.next = ListNode()
                ret = ret.next
            l1 = l1.next

        while l2:
            sumQ = l2.val + (1 if carry else 0)
            if sumQ >= 10:
                sumQ -= 10
                carry = True
            else:
                carry = False
            ret.val = sumQ
            prev = ret
            if l2.next:
                ret.next = ListNode()
                ret = ret.next
            l2 = l2.next

        if carry:
            prev.next = ListNode(1)

        return head

