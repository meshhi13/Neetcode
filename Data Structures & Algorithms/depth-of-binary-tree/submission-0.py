# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxLen = 0

        if not root:
            return maxLen

        return self.maxDepthHelp(root, 0)

        
    def maxDepthHelp(self, root, curLen):
        if not root:
            return curLen

        return max(self.maxDepthHelp(root.left, curLen + 1), self.maxDepthHelp(root.right, curLen + 1))

