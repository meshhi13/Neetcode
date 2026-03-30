# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []
        q.append(root)
        while q:
            level = []
            qLen = len(q)

            for i in range(qLen):
                newNode = q.pop(0)

                if newNode:
                    q.append(newNode.left)
                    q.append(newNode.right)

                    level.append(newNode.val)
                    
            if level:
                res.append(level)

        return res

