# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cur = root
        queue = [cur]

        while queue:
            level = []
            qLen = len(queue)
            for i in range(qLen):
                cur = queue.pop(0)
                if cur:
                    level.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)

            if level:
                res.append(level)
        
        return res
