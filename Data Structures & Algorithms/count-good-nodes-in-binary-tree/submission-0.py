# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, prev_val):
            nonlocal res

            if not node:
                return

            if node.val >= prev_val:
                res += 1
            
            prev_val = max(prev_val, node.val)
            dfs(node.left, prev_val)
            dfs(node.right, prev_val)
        
        dfs(root, root.val)
        return res
        