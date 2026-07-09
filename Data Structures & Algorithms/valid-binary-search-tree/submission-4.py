# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(root, interval):
            if not root:
                return True

            print("ROOT", root.val, "MAX", interval[1], "MIN", interval[0])

            ret = True

            if root.left and (root.left.val >= root.val or root.left.val >= interval[1] or root.left.val <= interval[0]):
                ret = False
            if root.right and (root.right.val <= root.val or root.right.val <= interval[0] or root.right.val >= interval[1]):
                ret = False

            return ret and isValidBSTHelper(root.left, [interval[0], root.val]) and isValidBSTHelper(root.right, [root.val, interval[1]])

        return isValidBSTHelper(root, [-math.inf, math.inf])