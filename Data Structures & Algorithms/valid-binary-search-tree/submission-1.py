# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            curr, l, r = q.popleft()

            if not (l < curr.val < r):
                return False

            if curr.left:
                q.append((curr.left, l, curr.val))
            if curr.right:
                q.append((curr.right, curr.val, r))

        return True