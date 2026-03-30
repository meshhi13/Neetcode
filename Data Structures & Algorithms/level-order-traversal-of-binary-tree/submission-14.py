# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [root]

        while queue:
            level = []
            qLen = len(queue)
            for i in range(qLen):
                newNode = queue.pop(0)
                if newNode:
                    level.append(newNode.val)
                    queue.append(newNode.left)
                    queue.append(newNode.right)

            if level:
                res.append(level)

        return res