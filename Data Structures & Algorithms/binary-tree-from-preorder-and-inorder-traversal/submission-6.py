# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {x: i for i, x in enumerate(inorder)}
        in_start, pre_start = 0, 0
        in_end, pre_end = len(inorder) - 1, len(preorder) - 1

        def construct(in_start, in_end, pre_start, pre_end):
            if (in_start > in_end) or (pre_start > pre_end):
                return None

            in_root = in_map[preorder[pre_start]]# Inorder root index
            remaining_left = in_root - in_start

            node = TreeNode(preorder[pre_start])
            node.left = construct(in_start, in_root - 1, pre_start + 1, pre_start + remaining_left)
            node.right = construct(in_root + 1, in_end, pre_start + remaining_left + 1, pre_end)

            return node

        node = construct(in_start, in_end, pre_start, pre_end)
        return node