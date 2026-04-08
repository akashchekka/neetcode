# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        head = root

        q = collections.deque()
        q.append(head)

        res = []
        while q:
            qlen = len(q)
            subnodes = []
            for i in range(qlen):
                temp = q.popleft()
                subnodes.append(temp.val)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
            
            res.append(subnodes)

        return res