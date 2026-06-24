"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashset = {}

        def recurseRandomList(head):
            if head == None:
                return

            if head in hashset:
                return hashset[head]
    
            res = Node(head.val)
            hashset[head] = res

            res.next = recurseRandomList(head.next)
            res.random = recurseRandomList(head.random)

            return res

        return recurseRandomList(head)
