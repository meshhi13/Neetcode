# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        queue.append((root, 0))
        level = 0

        res = []
        traverse = []
        currentTraverse = []

        while queue:
            cur, curLevel = queue.pop(0)

            if curLevel > level:
                traverse.append(currentTraverse)
                currentTraverse = []
                level += 1     

            if cur:
                queue.append((cur.left, curLevel + 1))
                queue.append((cur.right, curLevel + 1))
                currentTraverse.append(cur.val)       
                
        for i in traverse:
            if len(i) > 0:
                if i[-1]:
                    res.append(i[-1])

        return res



