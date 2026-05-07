# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lis = []
        counter = 0
        for i in lists:
            while i:
                lis.append((i.val, counter, i))
                i = i.next
                counter += 1

        heapq.heapify(lis) 

        result = ListNode()
        current = result
        while lis:
            nod = heapq.heappop(lis)[2]
            current.next = nod
            current = current.next

        return result.next