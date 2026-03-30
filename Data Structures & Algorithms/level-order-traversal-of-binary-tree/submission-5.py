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
            qLen = len(q)
            level = []
            for i in range(qLen):
                newNode = q.pop(0)
                
                if newNode:
                    level.append(newNode.val)
                    q.append(newNode.left)
                    q.append(newNode.right)

            if level:
                res.append(level)
        
        return res
        