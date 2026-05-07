# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def path_traverse(node: Node):
            nonlocal res

            if not node:
                return 0
            
            left = max(0, path_traverse(node.left))
            right = max(0, path_traverse(node.right))

            res = max(res, node.val + left + right)

            return node.val + max(left, right)
        
        path_traverse(root)

        return res