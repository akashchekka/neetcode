# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        def verify(root1, root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            return (True and 
                    verify(root1.left, root2.left) and 
                    verify(root1.right, root2.right))

        def inorder(root):
            if not root:
                return False

            if root.val == subRoot.val:
                if verify(root, subRoot):
                    return True

            return inorder(root.left) or inorder(root.right)

        return inorder(root)