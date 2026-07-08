# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTreeRec(head, preorder, inorder):
            if not preorder or not inorder:
                return None

            current = TreeNode(preorder[0])
            if preorder[0] in inorder:
                index = inorder.index(preorder[0])
                current.left = buildTreeRec(current.left, preorder[1: index + 1], inorder[:index])
                current.right = buildTreeRec(current.right, preorder[index + 1 :], inorder[index + 1:])
            return current

        return buildTreeRec(TreeNode(), preorder, inorder)
