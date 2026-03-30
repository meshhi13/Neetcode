# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        visit = [False]

        while stack:
            cur, v = stack.pop(), visit.pop()

            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    stack.append(cur.right)
                    stack.append(cur.left)
                    visit.append(True)
                    visit.append(False)
                    visit.append(False)

        return res
                