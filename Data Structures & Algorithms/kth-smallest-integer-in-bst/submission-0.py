# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp = root
        c = 0
        res = 0

        def traverse(node):
            nonlocal c, res
            
            if not node:
                return 

            traverse(node.left)

            c += 1
            if c == k:
                res = node.val
                return

            traverse(node.right)

        traverse(root)
        return res           
            