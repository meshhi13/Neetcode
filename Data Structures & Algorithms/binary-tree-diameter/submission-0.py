# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.diameterRec(root, 0)

    def diameterRec(self, root: Optional[TreeNode], maxVal: int) -> int:
        if not root:
            return maxVal

        maxVal = max(maxVal, self.height(root.left) + self.height(root.right))

        return max(self.diameterRec(root.left, maxVal), self.diameterRec(root.right, maxVal))

        

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

        
