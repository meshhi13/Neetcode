# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def levelOrderTraversal(root, level):
            if not root:
                return

            if len(res) <= level:
                res.append([])

            res[level].append(root.val)
            levelOrderTraversal(root.left, level+1)
            levelOrderTraversal(root.right, level+1)

        levelOrderTraversal(root, 0)
        return res
